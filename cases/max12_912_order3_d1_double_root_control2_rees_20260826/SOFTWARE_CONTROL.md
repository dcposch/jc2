# V1 software control — no mathematical endpoint

V1 is permanently non-promotable.  Its wrapper directed
`/usr/bin/time -v` telemetry into `singular.stderr` while simultaneously
requiring that file to be empty.  Therefore every completed solve failed its
own custody contract even when Singular itself returned rc zero.

- Box02 A was stopped after the defect was found: solver rc `1`, stdout SHA
  `52409654de70678894363935830fdb4ed97d271a291f018534bdeb71099dba97`,
  stderr SHA
  `3d4bcf56abfb2f5810cf221d291f12f017de4d0fa02445a3f41ae72b38cc33f0`.
- r6d B finished its underlying Singular command at rc `0` and printed a
  provisional residue-unit probe, but the wrapper correctly emitted
  `SOLVE_FAILED`; stdout SHA
  `190b696e210f7c230f955d46cd9457d2784ac55046a3e0f0d7109de332217dd4`,
  stderr/timing SHA
  `61a6861fc1bf875975a178ce80aa3abea540cc7c90e53aed8a2f73b3c4ccbbb7`.

Neither stream is evidence for lift or no lift.  V2 separates timing output,
adds torus saturation and basis custody, and reruns both encodings under new
tags.

