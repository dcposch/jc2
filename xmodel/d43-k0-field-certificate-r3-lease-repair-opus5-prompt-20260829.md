# Opus 5 repair — K0 certificate R3 lease ownership

You produced R2. Work from `/Users/dc/code/math/jc2` and write a fresh,
immutable R3 packet plus exactly this report:

`xmodel/d43-k0-field-certificate-r3-lease-repair-opus5-20260829.md`

Target packet:
`cases/d43_k0_field_certificate_r3_20260829/`

Read R2, your R2 report, and the complete different-model review
`xmodel/d43-k0-field-certificate-r2-hostile-review-fable5-20260829.md`.
Treat R2 as immutable. Copy to the new packet, then repair every blocking and
low-risk directly adjacent finding identified by the reviewer without changing
the mathematical engines or authorization semantics.

The blocking defect is exact: the service runs as `User=jc2k0`, while
`claim_authorization_lease` requires the run parent to be root-owned and not
group/world-writable and then tries to create the lease in that parent. Design
one satisfiable privilege boundary. Prefer a root-created, root-owned sealed
parent plus an explicitly precreated service-owned per-run working directory
and a root-owned/no-replace authorization or claim primitive whose exact
creation/consumption protocol is enforced outside the unprivileged process.
If a simpler design is safer, justify it. Do not weaken the parent-owner gate
or grant broad write permission merely to make the test pass.

Add fail-closed fixtures that exercise the real systemd UID/GID and POSIX
directory permissions, not mocked ownership alone: successful one-time claim,
second-claim refusal, wrong owner/mode refusal, service inability to alter the
root-owned authorization object, crash/restart semantics, and proof that a
failed pre-lease attempt does not burn authorization. Resolve the review's
minor GP constant-true line if safely mechanical; record but do not overfit
cosmetic/model-name items. Preserve unconditional-vs-conditional theorem
separation and every R2 mathematics hash unless a documented repair requires
regeneration.

Produce a fresh manifest, source seal, archive, preflight, ordinary/`-O`
tests, hostile mutations, and exact commands/counts. The report verdict may
be only `SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW` or `REPAIR_INCOMPLETE`;
R3 itself cannot authorize AWS. Include full/body hashes and an R2-to-R3
file/function diff inventory.

Hard boundaries: no AWS, GP execution, commit, push, canonical edits, heavy
CAS, or local long/high-memory process. Never access/list/search/build/status
or control `jc2-lean`; never run global `git status` or workspace-wide
searches. Modify only the requested R3 report and packet; use `/tmp` for
scratch.
