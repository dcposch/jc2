# GGV `8_28` lower FACEPIN / LF40 compiler v1, target-fix R1

This isolated case implements the reviewed actual-family lower compiler.  Run
the desk gate first, then the deterministic compiler:

```text
python3 -B cases/ggv_8_28_lower_facepin_lf40_v1_20260827/facepin_custody_gate.py ROOT OUTPUT
python3 -B cases/ggv_8_28_lower_facepin_lf40_v1_20260827/compile_lf40.py ROOT OUTPUT
```

The current frozen local outputs are `desk_gate/` and `compiled/`.  The latter carries
literal recurrence contributions, a disjoint original-coordinate Jacobian
replay, FACEPIN-substituted rows, exact generator/variable censuses, mutation
results, and the sequential exact-Q Singular program.

The original R0 generated Singular program omitted the constant term in the
single inhomogeneous equation `Dtil_17=-1`, even though the JSON rows and
compiler result recorded the correct target.  That AWS lane was stopped
without a mathematical verdict.  `TARGETFIX_R1_ERRATUM.md` records the exact
failure and repair.  The compiler now applies `with_target(...)` when emitting
every solver row and refuses to finish unless the generated row-17 ideal
contains the inhomogeneous target.  `SOURCE_FREEZE_TARGETFIX_R1.sha256` is the
current source manifest; the unqualified R0 freeze and archive are retained
only as immutable historical evidence.

Heavy algebra is AWS-only.  `run_lf40_aws.sh` refuses non-EC2 execution,
requires the preregistered envelope, replays every source/gate/compiler hash,
and stops at the first exact inconsistent prefix or a full row-40 proper
fixture.  All statuses remain producer-unreviewed until independently
replayed.
