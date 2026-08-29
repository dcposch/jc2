# Registration: `r=1` / symbolic-`d=1` V8 isolated-process replay

Date: 2026-08-26

## Purpose

V1--V7 passed every source, Faber-row, scaling, and recurrence sentinel before
the final symbolic `d=1` root-chart block, then failed closed with Singular's
`poly ^ number` diagnostic.  The same root algebra works in a fresh process.
The only relevant structural difference is that the combined V7 input first
loads `primdec.lib` for the independent `r=1` radical calculation; Singular
library state persists across later ring declarations.

V8 pins the immutable V7 compiler and source manifest, compiles the exact same
bytes on AWS, and splits the generated input at the unique `ring Rd1=` anchor.
It runs the `r=1` prefix and `d=1` suffix in two distinct Singular processes.
The compiler fails unless `primdec.lib` occurs exactly once in the `r=1`
script and zero times in the fresh `d=1` script.  No polynomial, coefficient,
row, chart ideal, or mathematical validator is changed.

## Preregistered endpoints

- The `r=1` process must pass all seven complete-source/Faber rows, the
  denominator recurrence and numerator identity, and the localized reduced
  support calculation on `D(p*k0)`.
- The fresh `d=1` process must pass all seven complete-source/Faber rows at
  grades 15 and 16, all three symbolic shift modules, both denominator
  recurrences, both deck root orientations, and the unmatched double-pole
  identity.
- Both exact Q and the independent `F_65521` replay must return engine `rc=0`
  with no `?` or `=FAIL` diagnostic.  Exact Q alone carries any
  characteristic-zero conclusion.

## Placement and caps

Run only on registered AWS hosts.  Each lane has a 24-GiB virtual-memory cap,
600-second compile cap, and 3600-second cap for each isolated Singular
process.  A timeout or any missing/nonunique sentinel is no verdict.

## Firewall

Even a full PASS is only a producer result for the normalized `r=1` leading
receiver and the symbolic unique-`AC`, `d=c-a=1` receiver on `D(p*k0)`.
It is not yet hostile-review promotion, fan exhaustiveness, a statement at
`p=0` or `k0=0`, a zero/infinity receiver, closure of the square branch,
exact order two, maximum twelve, or JC2.
