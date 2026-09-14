# Restore dependency path admission before file reads

Owner: /root/complete_lateflow_sol. ROOT collects and performs different-model
static delta review. Original reserve 08:33 UTC; hard stop 08:35 UTC today,
2026-09-13. Record actual first action and writer-idle UTC. No extension.

ROOT has independently confirmed your previous completion, read custody first,
verified all pins and the expected manifest, and read the whole source/report.
The requested path exception and durable diagnostics are present. One concrete
regression prevents acceptance: identity() now opens/hashes an arbitrary resolved
dependency before checking whether that path is permitted. A rejection after
reading does not preserve the old read boundary.

In a NEW preflight.py in THIS box, copy the prior derivative and make only this
ordering correction: after resolve and the durable IDENTITY_BEGIN, reject every
path outside /usr and /lib except the exact pinned sitecustomize path BEFORE
opening it. For that sole exception, check regular-file status and root-owned,
non-group/other-writable ancestry BEFORE opening it; compare its SHA after
hashing. Keep IDENTITY_COMPLETE only after all checks. Preserve every other
byte where possible. No new framework, controls, optional hardening or science.

Frozen input box/f10-mixed-preflight-diagnostics-sol-20260913/preflight.py
SHA256 8d659c1adf6f966202fce4717efd230d38b388e52f9767b0d0a6ea1af5f38f5e.
Previous task/report/custody and COORD snapshot may be reused at their unchanged
pins. Do not edit immutable predecessor packets, runner, observer, shared ledgers,
legacy user-dirty files, or any protected/baked tree/mirror. No AWS action, local
interpreter/import/AST/syntax/CAS/test execution, new agent, or execution authority.
The unchanged administrative finalizer alone is allowed.

Use apply_patch, freeze source/PINS/custody read-only, and publish the short
report xmodel/f10-mixed-preflight-order-sol-20260913.md with the unchanged
begin/close/finalize/expected-verify transaction at basis
0d39df3c9fd69c939a8420c54d03228b9077777d. Read all output bytes and recheck pins.
Return custody SHA first; source/report/manifest pins; actual ALL WRITERS IDLE.
This bounded correction grants no third worker, retry, or larger cap.
