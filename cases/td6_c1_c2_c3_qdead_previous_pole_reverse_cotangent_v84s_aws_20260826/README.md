# TD6 V84S reverse-presentation cotangent control

This case preserves the preregistered independent presentation check launched
after the V84R2 ten-pair table.  It uses the same source-typed quadratic
compiler but replaces FIRST and previous/pole elimination by a separately
coded reverse-source-row/reverse-existing-pivot route.  It reads no frozen
V84R2 table value and replays every resulting pivot/dependent row from the
original source rows.

The producer is currently active on AWS.  Until rc 0, a complete emitted
table, and custody freeze, this directory carries source and launch evidence
only and has no mathematical verdict.

This is a presentation/cotangent check, not a full Spencer-cohomology or
formal-involutivity computation.  Scope remains the fixed source-typed A3
section on the same generic principal open, through previous/pole, for the ten
`Sym^2(q2,q3,q4,q5)` pairs.  It says nothing about current, rank-drop fibres,
a nonlinear family, TD6, SP-2, landing, or JC2.

Heavy computation is AWS-only.  No `jc2-lean` file is a dependency or was
accessed by this lane.
