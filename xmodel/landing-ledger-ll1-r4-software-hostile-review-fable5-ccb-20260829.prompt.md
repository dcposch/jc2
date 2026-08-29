# Hostile software review — LL1-R4 full-actual-floor packet

You are Fable 5 acting as a different-model hostile software reviewer. Work
from basis `ccb6cd52eeab95f169b40f0a48668c3acd7a607e` and review only the exact
packet below. Do not read any current `ideation-20260829T1224Z-*` lane
prompt/log/report.

Software producer report:

```text
c2d627a002d9bb60cb467e65b5ffebc8969dba9bcde0ded1fb1426f5db72fbf5  xmodel/landing-ledger-ll1-r4-full-actual-floor-software-report-sol56-20260829.md
body 6753 / f645432f935fd39515ae3c59f8c4835dac8181fe5b6eed051e2012a04438b43a
23e56710ad5ba6e2b8a0c9e8e2a4cb802f7ef545dadea22164f9aacdb185998a  cases/landing_ledger_ll1_r4_20260829/MANIFEST.sha256
```

Review every file under `cases/landing_ledger_ll1_r4_20260829/`, its frozen
R3/legacy inputs, and the eight evidence pins declared in the report. The
math carrier inputs are already promoted; this task decides only whether R4
faithfully and safely implements their LL1 consumer.

Recompute rather than opine. Attack carrier leakage from
`FULL_ACTUAL_FIRST_SEPARATION` into generic `REPRESENTATIVE`, epsilon/zero, or
pure-epsilon rows; lower-floor versus attainment metadata; all 16 component
prices; exact four-mover exhaustiveness; old/new graph replay; six removals,
no additions, and `13->7`; frozen-R3 parity; evidence/source mutation closure;
manifest determinism; independent-validator independence; and load-bearing
`assert`/optimized behavior. Run compiler, validator, acceptance suite, and
legacy checker in ordinary and `-O` modes. Add targeted negative mutations.
Do not rerun the historical heavy engine or infer occurrence/completeness.

Return `PASS`, `PASS_WITH_REPAIR`, or `FAIL`, exact hashes/output hashes, any
counterexample, and maximum safe software promotion. Do not modify sources,
canonicals, code, or any other file. No web, AWS, heavy CAS, or `jc2-lean`
access.

Write exactly:

`xmodel/landing-ledger-ll1-r4-software-hostile-review-fable5-ccb-20260829.md`

Seal the report body with exact byte length and SHA-256 if possible.
