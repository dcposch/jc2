# VERIFICATION.md — re-running the gate suites of the theory bundle

Every promoted arithmetic claim in the document corpus has a named check in
one of the gate suites below. All suites are pure Python 3 standard library
(exact `int` / `fractions.Fraction` arithmetic, no floats, no network), run
from the bundle root, and exit 0. Total wall time for the full list is about
four minutes on a laptop (the two slow suites are marked). Verified against
Python 3.9+ on macOS; the scripts use nothing platform-specific.

Run everything from the bundle root (the directory containing this file):

```bash
cd jc72108-theory-bundle-v1
```

## The gate suites

| command | expected final line(s) | checks | wall |
|---|---|---|---|
| `python3 cases/tower_check.py` | `RESULT: ALL CHECKS PASS (incl. perturbation suite) ... UNIFORM (17 cells): THEOREM` | 1559 uniform-mode checks + 5 certificate suites + 21 perturbations | ~4 s |
| `python3 cases/tower_rollout_arith.py` | `census parity over 16 cells: PASS` + `GLOBAL: max chain-2 gap over all 16 cells = 2/5 (< 1/2: True); min stack product = 7; empty-stack escapes: 0` | prediction table | ~1 s |
| `python3 cases/td7_census_e5.py` | `ALL GATES PASS (G1 grok replay, G2 six-cell E5 re-solve, G3 BOOK-pin parity 62/53/35, G4 positive controls, G5 negative controls x2 readings)` | G1-G5 | ~50 s |
| `python3 cases/tower_td11.py` | `RESULT: ALL 66 TOWER-TD11 CHECKS PASS` | 66 | ~2 min |
| `python3 cases/td11_census.py` | `RESULT: ALL 24 CENSUS CHECKS PASS -- 411 td-11 rows stamped dead, 2 remaining classes (FC2/FC4/FC5/FC6/FC7 discharged; FC1-R fleet-emitted), 17/17 td-7 regression` | 24 | ~1 s |
| `python3 cases/td12_book.py` | `RESULT: ALL 14 TD12-BOOK CHECKS PASS -- 14/14 dead (6 spine + 8 first-death-refused), 0 live` | 14 | ~1 s |
| `python3 cases/nfz_check.py` | `RESULT: ALL 39 NF-Z CHECKS PASS` | 39 | ~1 s |
| `python3 cases/nfd_check.py` | `RESULT: ALL 22 NF-D CHECKS PASS` | 22 | ~1 s |
| `python3 cases/nfm_check.py` | `RESULT: ALL 25 NF-M CHECKS PASS` | 25 | ~1 s |
| `python3 cases/nfp_check.py` | `RESULT: ALL 10 NF-P CHECKS PASS` | 10 | ~1 s |
| `python3 cases/depthstab_check.py` | `RESULT: ALL 14 DEPTH-STAB CHECKS PASS -- route B committed (D*_eff = 2e+1, e measured), route A structural; D* >= 23 forced by the data` | 14 | ~1 s |
| `python3 cases/tdbound_scan.py` | `RESULT: ALL 6 TDBOUND CHECKS PASS -- law (i) unfalsified, frontier at equality, the td-12 (3,5) entry named` | 6 | ~1 s |
| `python3 cases/transport_check.py` | JSON certificate with `"status": "PASS"` | regression fixture for TRANSPORT.md's worked data (not a proof of its Theorems 1.1/2.1/3.1) | ~1 s |
| `python3 cases/am_check.py` | `21 checks, 0 FAIL` + the forced characteristic sequence | 21 | ~1 s |
| `python3 cases/witt_check.py` | `SELF-TEST PASS` + `registered stratum: 1152 nonzero / 0 vanishing` | full-stratum sweep | ~4 s |
| `python3 cases/residue_check.py mathieu` | `MATHIEU OK` | M1-M8 (Theorem A machine layer) | ~30 s |

Notes on the interesting inputs:

- `cases/tower_check.py` consumes the five frozen tower certificates in
  `cases/towers/*.json` and the pricing layer in
  `cases/scratch_offaxis_pricing/` (read-only). Its final line is the td-7
  uniform tower theorem's machine verdict.
- `cases/depthstab_check.py` gate DS1 re-verifies the 38-row byte-identity
  between the D21 CORE2 emissions and the D23-core emissions at all three
  primes, directly against `cases/directionb_core2_p*.ms` and
  `cases/directionb_core23_p*.ms` in this bundle.
- `cases/td11_census.py` re-derives the full 411-row td-11 census and its
  stamp multiset (185 OUTER-DEAD / 133 SPINE-DEAD-H8 / 63 UNREALIZABLE /
  12 SELF-REFUSED / 11 CLASH-DEAD / 7 SPLIT), and replays the 17-cell td-7
  book through the same engine as a regression.

## What is frozen but not re-run

- **Groebner-basis solver verdicts (msolve 0.10.1).** The `.ms` files under
  `cases/` are the frozen solver inputs (msolve input format; the matching
  `.rows.txt` files are the human-readable row legends, since `.ms` carries
  no comments). The banked verdicts quoted in the corpus: the a3-chamber
  double-EMPTY (`GB = [1]` at p105337 and p200257,
  `cases/directionb_residual32_nolog_leaf_a3_p*.ms`); the D21 CORE2 fiber
  NONEMPTY at all three primes (397-element Groebner basis, frozen in
  `cases/directionb_fiber_gb_p105337.out.txt` with the 12 sample points in
  `cases/directionb_fiber_points_p105337.txt`); the D23-core lanes TIMEOUT
  at 12 h caps (verdict pending, stated as such everywhere). To replay a
  solver verdict: `msolve -g 2 -f <file>.ms` (mod-p files carry their prime
  in the header line).
- **The emission engines.** `cases/fastelim.py` (the python-flint band
  elimination engine, 22 unit pivots, gates G0.1-G0.7),
  `cases/directionb_row22_schur.py`, `cases/directionb_row22_emit.py`,
  `cases/directionb_core23_{elim,emit,final}.py`, and
  `cases/directionb_fiber_filter.py` are included for provenance and audit.
  Re-running them end to end needs `python-flint >= 0.9.0` plus the frozen
  depth-21 window data (`directionb_tails_D21.pkl`,
  `directionb_window_conditions.pkl`, bundle root) and, for some stages,
  session-state pickles regenerated by `cases/directionb_window.py`; the
  frozen `.ms`/`.txt` artifacts in this bundle are their verified outputs
  (byte-identity and round-trip gates in `cases/depthstab_check.py` and the
  corpus record in `SHEET6-DIRECTIONB.md` sections 7.S-8.S2).
- **Fleet lanes.** Long-running solver lanes (the D23 verdict runs, the
  FC1-R beyond-core audit) are executed on remote iron; their state at
  bundling time is recorded honestly in `notes.md` and
  `SHEET6-DIRECTIONB.md`. No claim in `SUMMARY.pdf` depends on a pending
  lane.

## Cross-checking a claim

To trace any statement in `SUMMARY.pdf`: (1) the section cites the corpus
document (bundle root) that states it precisely with its status header;
(2) that document names its machine gate under `cases/` and its review
chain under `xmodel/`; (3) the gate suite prints a named `[PASS]` line for
each load-bearing arithmetic fact. The promotion ledger is `AUDIT.md`; the
dated lab journal is `notes.md`; the hostile foundations audit is
`REDUCTION.md`.
