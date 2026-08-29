# Opus 5 — K0 certificate R4 mint/dry-run choreography repair

Work only in `/Users/dc/code/math/jc2`. Repair R3 in a fresh immutable R4; never mutate R3.

Read in full:

- `xmodel/d43-k0-field-certificate-r3-lease-repair-opus5-20260829.md`
- `xmodel/d43-k0-field-certificate-r3-hostile-review-grok46-20260829.md`
- every R3 source/manifest/review-request file in `cases/d43_k0_field_certificate_r3_20260829/`.

Preserve all R3 mathematics and the reviewed custody boundary. Fix the single blocking deployment-order defect: the sealed authorization template currently says external root mint -> service dry-run -> unit start, while the unit repeats `ExecStartPre=+` mint, so an honest launch necessarily dies `MINT_ALREADY_SPENT`.

Prefer one atomic systemd choreography unless a stronger design is proved:

1. root `ExecStartPre=+` mints exactly once;
2. a non-`+` service-user `ExecStartPre` runs `custody_selftest --on-host-dry-run` against that token without burning it;
3. `ExecStart` runs the supervisor, which verifies then burns/leases;
4. root `ExecStopPost=+` retires/seals evidence.

The authorization template, unit, preregistration, static pins, mutations, and replay instructions must describe exactly this one path; no external pre-mint is allowed. Prove the dry-run is executed as the service identity under the intended sandbox and cannot consume the one-shot claim. Add a mutation that restores the double-mint order and must fail, plus ordering/identity/one-shot controls. Preserve the fail-closed spent-first semantics and do not move the dry-run into `run_job`.

Also carry the review's residual symlink-ancestor, GP-unparsed, systemd-unexecuted, and root-object debts honestly; do not solve them by weakening the gates. No AWS, GP, CAS, canonical edit, commit, push, or nested formalization-tree access.

Write packet `cases/d43_k0_field_certificate_r4_20260829/` and report `xmodel/d43-k0-field-certificate-r4-choreography-repair-opus5-20260829.md`. End at `SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`; include exact R3-to-R4 diff, ordinary/`-O` bounded tests, hostile mutations, deployment sequence, scope firewall, and body/full SHA-256 seals.
