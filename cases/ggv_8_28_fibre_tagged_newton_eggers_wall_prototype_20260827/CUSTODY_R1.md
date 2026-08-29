# Custody R1 after `TRANSPORT.md` editorial errata fold

Date: 2026-08-27

The frozen R0 producer correctly failed its source-pin guard after the
coordinator folded the already-filed hostile review's non-load-bearing
errata into `ladder/TRANSPORT.md`.  No R0 file or digest was rewritten.

`verify_r1.py` is a custody-only wrapper.  It pins the exact R0 verifier,
changes only the expected `TRANSPORT.md` digest from `39a607c8...` to
`9750aa9d...`, runs the complete unchanged R0 mathematics, and requires the
returned object to equal frozen `RESULT.json` exactly.  This does not repair,
strengthen, or promote the non-Keller prototype; it only distinguishes an
approved contextual-document drift from mathematical drift.

Exact replay: `PASS`, with `mathematical_result_unchanged=true`.

- R1 wrapper SHA-256: `7c1205ff3247e06c31729c22a65c39b1e5bf3bd99e28d5fe6a7780ab3ac315b5`
- Frozen mathematical result SHA-256:
  `deb3a6308e07137c4113a45d4edafdd7a0be34d954d600b33d85ddb8acba57bd`
- Current reviewed-errata `TRANSPORT.md` SHA-256:
  `9750aa9d14650a22a410803022d42fa523e3993a21ee9a27714386fa1150047c`
