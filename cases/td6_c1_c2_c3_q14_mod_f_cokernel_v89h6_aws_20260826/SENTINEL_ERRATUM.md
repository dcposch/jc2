# TD6 V89H6 initial coefficient-type sentinel erratum

Date: 2026-08-26

The first dual deployment used source archive
`63f599d443b3cb396cca4e26b9391c90bec8b712d157aba676452d58f9e9e9a6`
and terminated identically with rc 1 after completing the exact source
rebuild, denominator audit, full specialized FIRST inverse, 38-pivot P12
division, and original-FIRST replay.

The failure was a reporter/type sentinel immediately after that replay.
`v87.q_constant` returns an `E3` coefficient, but the client tried to inspect
it as a `QPoly` through `.coefficients`.  No positive-class or good-prime
verdict was emitted.

V89H6R1 replaces those two reporter lines by the exact field-unit check
`base_unit.inverse()`.  The failed client, source manifest/archive, and both
AWS run directories are preserved under `sentinel` names.  R1 requires a new
manifest/archive and fresh dual roots.
