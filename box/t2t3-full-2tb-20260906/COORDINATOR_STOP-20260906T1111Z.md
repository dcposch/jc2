# Coordinator disposition: stop the unfinished full direct input build

Root Astra, 2026-09-06T11:11:10Z. This is a coordinator operator stop, not
an OOM, a mathematical decision, or permission to restart the same build.

On protected worker i-025410e620b1d65c9,172.30.0.103, root revalidated
Python PID4923, PPID4921, PGID4917, start08:48:49, exact command
`/usr/bin/python3 -u /home/ubuntu/t2t3-full/drivers/build_direct_whole.py --case 99-delta2 --output /home/ubuntu/t2t3-full/presentations/full`.
Only that monolithic Python process received SIGTERM. Its time/bash wrappers
were left intact to write the existing completion receipts. No other CAS
process was on this worker in the pre-stop inventory.

Reason: at11:10Z, elapsed141minutes, roughly2TiB resident plus737GiB swap,
with no new stdout progress since08:52:26 (400 T2_upper rows), no closed
full input and no solver. Labels remained0bytes, .ms55,245,012bytes,
.sing73,006,401bytes. The input construction is not providing enough
information to justify continued memory growth. A separately built complete
physical-J representation has now passed different-model review and root's
exact all-row replay; a bounded full-ideal solver comparison replaces this
construction attempt. This is not a claim of T2/T3 equivalence.

Retain all partial inputs, driver revisions, stdout/stderr/time/rc files and
compact custody. Do not delete or overwrite them. Record the termination as
COORDINATOR_STOP/NO_FULL_PRESENTATION/NO_SOLVER, never a unit or nonunit.
Root will verify process exit and memory release; SIGTERM return by itself
does not establish cleanup completion.

The2TB instance is NOT terminated, retagged, or otherwise released. Its
DC-only instance-termination restriction remains. The separate .63 literal
subset solves and .73 b9q0 solves are UNTOUCHED. Do not restart, extend swap,
launch a replacement, or repurpose the worker in response to this stop;
return terminal custody to root first.
