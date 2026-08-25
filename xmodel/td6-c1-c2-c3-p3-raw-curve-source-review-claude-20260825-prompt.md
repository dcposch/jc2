# Hostile no-shell source review — TD6 raw `H=P3=0` closure

Act as a hostile different-model mathematical reviewer in
`/Users/dc/code/math/jc2`.  Do not use Bash, a shell, the web, or any local
computation.  Treat all existing bytes as immutable and write only the exact
output file named below.

First read the complete charge and all six attacks in
`xmodel/td6-c1-c2-c3-p3-raw-curve-review-claude-20260825-prompt.md`.  Perform
that review in full.  For source inspection, also read every regular file in

`cases/td6_c1_c2_c3_p3_raw_curve_source_snapshot_20260825/`.

This is a separately frozen, readable extraction of the archive that the
first prompt charges.  Verify its `MANIFEST.sha256`, `FREEZE.sha256`,
`DEPENDENCIES.sha256`, `payload/SOURCE.sha256`, and then inspect the full
producer/import closure rather than trusting the PASS markers.  Charged
supplement hashes are:

```text
supplement manifest     8e581d57d408cb881bb105a8b7a796cbe2aa2137c61a2a07e2d78d51afca30bb
supplement freeze file  63d875ab3918aa50d309b4191971ca02859d7283bd82c72ece058f229aaaabd0
supplement README       9e81509b78e47f69cb14f4a6e16f1b7be3423b7d69a9768ea3456afd6b6f7e4b
supplement dependencies 6cacc31931354dd9c17a61dae8102551c781e7cbf440817babb6b34f3ca85780
payload SOURCE          7b00ab87e35ca9b2cff9d31d7e0e75cd5cd4fbf5fbe64d1ad68f300c39a2032f
P3 producer             1b492ad26a2f1c0cdc3ae3983068639163118010ffba9e53c9e6d097d56c9a22
```

Pay special attention to whether the nested exact field is genuinely a
field/function-field model; whether all 7,589 inversions are checked in the
actual arithmetic path; whether the original-row lift and denominator LCMs
cover all of `D(U)`; and whether the earlier origin evidence composes without
being affected by the V14 B3 erratum.

State the smallest error or missing hypothesis if any.  Give one exact
promotable sentence with strict scope.  Write exactly
`xmodel/td6-c1-c2-c3-p3-raw-curve-source-review-claude-20260825.md`; edit no
other file.  End with exactly one verdict: `CONFIRMED`, `GAP`, or `REFUTED`.
