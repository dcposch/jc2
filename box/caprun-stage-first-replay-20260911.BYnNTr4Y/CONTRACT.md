# Fixed fourteen-file candidate transport

Producer-checked OFFLINE ONLY, pending FIRST review. This transports existing
candidate bytes; it neither binds physical observations nor installs or runs
the candidates. The accepted latebinder and all its caller duties are unchanged.

`stage_patch.make_patch(candidates, prefix)` accepts exactly the14 names in
NAMES, including SUMMARY.json. Each value is nonempty UTF-8 bytes ending in
LF, without CR or NUL, at most131072bytes; aggregate at most524288bytes.
SUMMARY must carry the existing schema, candidate-only status, false release
authority, HISTORICAL_TEST or ROOT_ATTESTED_CANDIDATE context, and exact
hash/size commitments for all13 other outputs. Duplicate summary keys reject.
No claim to semantically revalidate every summary field or document is made:
ROOT must authenticate the binder, inputs, outputs and its exact allowed edits.

The prefix is restricted to an absolute
`/home/ubuntu/jc2/box/caprun-stage-exercise-YYYYMMDD.<6--24 alphanumeric>` path.
The API does not access it. ROOT must create a NEW private directory with
mktemp -d, keep exclusive ownership/no concurrent writer, and ensure the14
target paths are absent. apply_patch's Add File is not an exclusive-file-create
primitive: do not use an existing directory or retry a partially applied patch.
Preserve partial output and its failed status; it is never installation evidence.

The patch contains only the fourteen allowlisted Add File paths. Every content
line receives a leading plus; embedded ASCII patch-looking lines stay content.
No byte is decoded as ASCII. The returned hash map covers all14 output files,
including SUMMARY itself, without self-hashing inside a file. ROOT requires
successful generation, HISTORICAL_TEST for the documentary exercise, successful
application and exactly14 distinct matching readback hashes before claiming
staging success. Tool truncation/JSON parse errors fail before application.
No general untrusted-template, filesystem-race or tool-implementation theorem.

`historical_exercise.py` is ONLY a historical-data fixture adapter. It pins
the existing helper/harness before import; the harness pins all8 historical
texts before use. It rejects a nonhistorical summary and prints JSON carrying
the patch, never applying it. ROOT authenticates this adapter and transport
before execution. Future actual-candidate callers are not implemented by this
fixture adapter. The pure transport API can accept correctly authenticated
ROOT_ATTESTED_CANDIDATE output, but that is not operational clearance.

Nine test methods exercise the old ASCII failure, exact reconstructed bytes,
all missing/extra files, all13 altered commitments, false summary fields,
duplicate keys, invalid text, unsafe paths, patch-looking content and preservation.
They are ordinary Python stdlib documentary tests only, not scientific execution,
optimized-mode verification or tests of the underlying runtime/holder.

One actual single functions.exec call generated and applied the patch in fresh
private directory caprun-stage-exercise-20260911.XXo03Rv3, then independently
hashed all14 files. Result:78889bytes,14 matches,400ms orchestrator elapsed
including mktemp/generation/apply_patch/readback. EXERCISE.json retains the
tool-observed record; RECIPE.js preserves the executed orchestration with
formatting and explanatory comments only. This
does NOT include AWS/SSH, actual observations, ROOT semantic review, remote
installation, liveness/release, holder startup or a complete120second cycle.
No speedup ratio or future timing guarantee is inferred. All candidate files
remain paired with their HISTORICAL_TEST summary and retained, never executed.

Next gate is one FIRST different-model review of this new boundary. No worker,
cap change, retry of batch b/c, new framework or automatic science follows.
