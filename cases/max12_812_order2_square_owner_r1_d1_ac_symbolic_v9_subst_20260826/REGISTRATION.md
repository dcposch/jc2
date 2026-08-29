# Registration: `r=1` / symbolic-`d=1` V9 direct-substitution replay

Date: 2026-08-26

V8 proved that `r=1` is clean in an isolated process, but the D1 root-chart
ideal declaration retained the same Singular `poly ^ number` diagnostic.
All source/Faber, scaling, and recurrence sentinels before that block passed
over exact Q and `F_65521`; therefore V8 remains a parser-negative control,
not a mathematical verdict.

V9 pins and invokes V8, retains its isolated processes, and changes only the
final D1 chart evaluator.  It replaces four quotient-ideal reductions by the
equivalent sequential substitutions used successfully in the frozen c3
client, with the c3-safe auxiliary names `rtx,aua,cvg` and explicit products
instead of powers.  The positive and deck-conjugate substitutions are
`p=-2*rtx*rtx`, `A=aua*(z-/+rtx)`, and
`C=cvg*(z+/-rtx)`.  All source rows, rational coefficients, symbolic shifts,
recurrences, scope, and acceptance sentinels remain unchanged.

Dual exact-Q / `F_65521` runs are preregistered on Box03/r6d, each capped at
24 GiB, 600 seconds compile, and 3600 seconds per isolated engine.  The
validator now rejects Singular diagnostics with arbitrary leading spaces.
A timeout, diagnostic, or missing sentinel is no verdict.

Even PASS is producer-tier only for the normalized `r=1` receiver and the
symbolic unique-`AC`, `d=1` receiver on `D(p*k0)`.  It is not fan closure,
square/order-two closure, maximum twelve, or JC2.
