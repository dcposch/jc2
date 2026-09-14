# Dummy live-limits attachment — inert source delta

The v2 probe preserves the exact CLI, fork/immediate parent exit, ignored TERM,
64MiB allocation and 4096-byte page touches, one combined post-touch marker/JSON
write, and infinite sleep. It adds no observer, handshake, loop, cap or library.

Before the marker, the child requires a single `0::/…` cgroup-v2 membership,
canonical traversal-free resolution beneath `/sys/fs/cgroup`, and an actual
directory stat identity. Each proc/cgroup metadata read is O_NOFOLLOW and at
most4096 bytes. The JSON adds cgroup namespace, resolved path and directory
device/inode/mode/uid/gid; exact control-file bytes; actual getrlimit pairs;
UID/GID, NoNewPrivs and CapEff. Every numeric value is a string.

Acceptance is CPU `(3,4)`, AS `(34359738368,34359738368)`, FSIZE
`(268435456,268435456)`, nonzero equal real/effective UID and GID,
NoNewPrivs1, CapEff all-zero, cpu.max `80000 100000`, burst0,
memory.max34359738368, swap.max0, cgroup.type domain and empty
cgroup.subtree_control. Controllers must be unique bounded ASCII tokens and
are retained exactly, not assumed. Missing, malformed, inaccessible, wrong or
oversized data raises before the marker and is STOP.

ROOT must compare the exact canonical two-line stdout against CAPRUN/service
identity, actual registration and terminal telemetry; bind the new probe hash;
and independently prove physical unit ancestry, nondelegation/no escape,
read-only cgroup custody, sampled RSS/TERM/KILL/reaping and terminal kernel
emptiness. Self-reported controls do not prove no escape or true peak. There is
no guarantee the marker wins the RSS-sampling race. Whole dummy25seconds
including cleanup and all original physical/native/tmpfs duties remain.
