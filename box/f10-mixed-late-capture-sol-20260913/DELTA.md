# Late capture/source delta

Status: INTERNAL / UNREVIEWED / UNEXECUTED / UNBOUND.

`dispatch.py` is byte-identical to dispatcher
`5cfff7e243482e2c5779b3d3af9ab716e4966adfadc70dcb988c079e208b52ed`
except for one ten-line insertion after all registration, host, clock, source,
path, empty-sibling, qualification, native-manifest and library checks, and
before `common`, `run`, the dummy, or any scientific phase.

The insertion flushes both Python streams; exclusively creates
`output/runner.stdout` and `output/runner.stderr` with `O_NOFOLLOW`, forces
mode 0600, duplicates them onto fds 1 and 2, and closes the temporary fds.
An existing name is never opened or overwritten. A failure is propagated to
the outer journal path. After both `dup2` calls, dispatcher diagnostics and
CAPRUN's own status lines use the bounded tmpfs files; each CAPRUN child's
stdout/stderr/telemetry remains in its already separate per-phase files.

`science-unit.template.sh` is a literal inert operator sequence. It creates
one fresh 256 MiB mount with exactly empty admin/output siblings, retains
journal startup until the dispatcher accepts the prefix and redirects itself,
arms the original absolute TERM/KILL before launch, invokes the exact root
dispatcher CLI with the DAC-corrected supervisor capability set, captures the
real `--wait` result and bounded unit diagnostic afterward, and demands
terminal cgroup emptiness/absence and completion before the original deadline.
All host, namespace, UID/GID, source, registration, unit and clock values are
placeholders. ROOT must authenticate them and perform live-control capture,
whole census/hash/fsync/durable transfer and exact retirement. No retry exists.
