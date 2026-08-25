# Clean-stop metadata

- Trigger: first direct-replayed SAT survivor at base 519 / `0201020`.
- Stop issued: `2026-08-25T08:09:15Z` on Box02.
- Explicitly TERM-stopped: 49 still-live per-base Boolector solver PIDs,
  global Boolector PID 105626, and Z3 4.16 PID 109156.
- Global Boolector endpoint at stop: signal 15 after 20:38.83, maximum RSS
  9,837,136 KiB; no SAT/UNSAT endpoint.
- Z3 4.16 128-GiB lane at stop: signal 15 after 8:06.57, maximum RSS
  28,042,964 KiB; no SAT/UNSAT endpoint.
- Earlier Z3 4.16 32-GiB lane: rc 101/OOM after 6:35.77, maximum RSS
  28,042,976 KiB; preserved remotely as a resource negative control.
- At clean stop, 30 base lanes had completed: 3 direct-replayed SAT and 27
  solver-only UNSAT.  The latter are not proof-certified and carry no theorem
  weight here.

No solver process under the global-predecessor job path remained after the
stop poll.
