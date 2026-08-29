# LF40 target-custody erratum and R1 repair

Date found: 2026-08-27  
Affected artifact: R0 `compiled/lf40_sequential_QQ.sing`  
Mathematical impact: **no valid conclusion; the affected AWS lane was stopped**

## Failure

The mathematical specification and serialized FACEPIN row data encoded

```text
Dtil_17=-1,
```

so the degree-zero equation is

```text
1+f_0_1*g_1_0-f_1_0*g_0_1=0.
```

R0's `singular_program()` instead serialized `face_rows[row][degree]`
directly and therefore emitted

```text
ideal ROW_17=f_0_1*g_1_0-f_1_0*g_0_1,...
```

The JSON compiler output was correct; the error lay only in the final
JSON-to-Singular serialization boundary.  Consequently the running R0
Singular process was solving a different homogeneous ideal.  Nothing from
that computation is admissible as support for consistency, inconsistency, a
lower fixture, or any JC2 claim.

## Containment

The R0 process on AWS `r6b` was terminated at
`2026-08-27T20:57:32Z`.  Its wrapper preserved a fail-closed terminal packet at
`aws_r6b_failed_wrong_target_v0/`:

```text
status             DEPENDENCY_SOURCE_REPLAY_OR_ENGINE_FAILURE
solver rc          1
validator rc       90
elapsed wall       2:01:36
maximum RSS        3,512,480 KiB
swaps              0
RESULT.json SHA    b78e6aad20bd7880d278313e2b161d0a1b511d931518b16c89d687b3dbd0744a
EVIDENCE SHA       9eef6aa288e52c9837c91642986d8f8bc2b58a251d313fd8f015de9bc065cca3
```

The original `SOURCE_FREEZE.sha256` and
`GGV_8_28_LF40_v1_source_20260827.tar.gz` are retained unchanged as R0
historical evidence.  They are retired from mathematical execution.

## Repair and independent replay

R1 applies `with_target(...)` to every polynomial passed to the Singular
serializer.  It also computes both the targeted and homogeneous row-17
strings and aborts unless they differ and the targeted string occurs at the
start of `ideal ROW_17`.

The patched compiler SHA-256 is

```text
828f819e78ba36cf019e7014263148a4ee53ffd5b77ef77fee310637b82fc719
```

It was staged independently on `r6b` and run from a fresh output directory.
The exact compiler replay completed in 5.31 seconds with maximum RSS 361,512
KiB and zero swaps, printed `PASS-LF40-COMPILER-CUSTODY`, and replayed every
entry in `COMPILER_EVIDENCE.sha256` successfully.  A directory comparison
against R0 found exactly two changed files:

1. `lf40_sequential_QQ.sing`, whose only content change is the added row-17
   constant `1`; and
2. `COMPILER_EVIDENCE.sha256`, whose only payload-digest change is the
   Singular program hash.

The corrected Singular program SHA-256 is

```text
435c350f8a5be062d9b1e1b7cf57e9483dcf2648400fe250d4edbd13ccf846f7
```

The AWS replay telemetry is frozen in `targetfix_compile_r1_aws/`.  A new R1
source freeze and archive are used for the corrected run; no R0 result or
partial basis is imported.
