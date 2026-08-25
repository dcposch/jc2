# Erratum: V33/V69 do not cover all of raw `U=0`

Frozen status: **nonmutating theorem-scope correction and dependency
quarantine.**

Hostile review SHA-256
`706f6ad408e680de1b0bb1d9b23c10e49829ab803a9bf06553253e4231b2e291`
found that the V33/V69 `U=0` transport used two pivots with numerator `-C`.
The true transport chart is therefore `D(C^2)`.  The printed denominator one
was only the residual/Bezout/combination LCM and cannot be promoted to a
complete chart.

The exact source-typed ranks, original row `('X-2',14)`, 14-row source
combination, beta-degree-zero unit obstruction, and V69 canonical serializer
survive on `U=0,D(C)`.  The raw stratum `C=U=0` was not run by V33/V69 and
cannot be obtained by specialization.  It is preregistered separately as
`u-h-zero`; its denominator-zero leaves must also be rebuilt raw.

This erratum supersedes the whole-`U=0` sentences in both frozen producer
reports and READMEs, plus the “all-beta `U=0` theorem remains valid” sentence
in the earlier staged-N13 localization erratum.  It quarantines every
all-beta whole-`H=0`, whole-`B3=0`, rational-line/curve endpoint, V68 endpoint
composition, and fixed-A3 union that consumed that claim.  It does not alter
their independently proved narrow opens, the V68 route equalities, or the
older separately stratified beta-zero atlas.

See
`xmodel/td6-c1-c2-c3-q2-beta-u-zero-scope-erratum-20260825.md` for the full
dependency statement.  No frozen predecessor byte is modified.
