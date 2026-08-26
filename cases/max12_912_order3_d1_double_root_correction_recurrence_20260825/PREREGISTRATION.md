# AWS preregistration: correction-control replay

Date: 2026-08-25

Run `verify_correction_controls.py` only on registered Amazon EC2.  It must
consume charged source SHA
`67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623`,
return rc zero and empty stderr, and print exactly one terminal marker
`PASS_D1_DOUBLE_ROOT_CORRECTION_CONTROLS`.

This replay tests two finite correction identities against all eight exact
ordinary source rows.  It neither proves their formal extension nor completes
the double-root Newton fan.
