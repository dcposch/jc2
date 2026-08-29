# V23 V1 control erratum

Date: 2026-08-27

The V1 local census failed closed after parsing and specializing all inputs but
before writing `RESULT.json`.  No mathematical mismatch was found.  Its
positive control compared the entire pure `(a0,qa1,rho)` chart polynomial to
the `A00` point value, forgetting that `A00` also sets `qa1=0`.

The failure exposed genuine information the census was intended to discover:
besides `Tg15_6=-a0^3/16` at `qa1=0`, five other grade-15 rows contain pure
`a0^3` terms multiplied by positive powers of `qa1` and even powers of `rho`.

V1 output directory `output/` is quarantined and has no result.  R1 pins and
imports the V1 parser/rewriter byte-for-byte, changes only the control
comparison to specialize `qa1=0`, and retains the full pure-chart census as
output.
