# Global `J`-power membership desk gate

- Basis and source are exactly those in `PREREGISTRATION.md` and
  `INPUTS.sha256`.
- Question: find the smallest `N` for which `J^N` is contained in `I` by
  testing global exact-Q ideal membership, starting at `N=16` and descending
  only while containment holds.  `J^17 subset I` is proved separately from
  the reviewed four fifth-power identities and is not inferred from this
  computation.
- Method: recompute one ordinary exact-Q standard basis of the seven-row
  ideal `I` in the original six variables; reduce every canonical generator
  of each tested `J^N`; stop on the first nonzero normal form and record its
  exact source generator and remainder.
- Prior resource calibration: the frozen AWS V4 producer computed the same
  standard basis in 3.21 wall seconds and 44,192 KiB maximum RSS.  This
  bounded desk rerun therefore uses `CAPRUN/v1` with 45 wall seconds, 45 CPU
  seconds, 1 GiB aggregate RSS, closed file stdin, and explicit `quit;`.
- Outcomes: failure at `N=16` plus the independent `J^17` proof establishes
  minimal exponent 17.  Containment at 16 triggers the next descending test.
  Any cap/error is `NO VERDICT`; no uncapped local retry.
- This gate does not compute the `J`-adic filtered standard basis or full
  initial ideal.  The live Fable hostile review owns that potentially heavier
  computation.
