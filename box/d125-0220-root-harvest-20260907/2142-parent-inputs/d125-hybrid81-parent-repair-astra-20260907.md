# D125 hybrid81 exact parent-argv repair

2026-09-07. PRODUCER-CHECKED engineering delta, not engineering GREEN.
No engine, authority, deployment, source, solver, or worker action occurred.
The pure-math packet is unchanged and outside this repair.

## Exact repair

The terminal Sol56 gate
`xmodel/d125-hybrid81-engine-gate-sol56-v2-20260907.md`
(SHA256 `081d92293a62b0e5a9616e62b28d510468cfef4c6d6972d6926c66cca5c8e23d`)
correctly refutes the old helper's claimed exact parent-argv enforcement:
membership of the runner pathname also admits changed caps and output paths.
I read that whole report, its 223-line checker, the whole 73-line helper,
registration, and accepted driver. This repair does not revise those inputs.

The new owned `box/d125-hybrid81-parent-repair-20260907/engine.py` adds only
`expected_parent_argv(operation)` and replaces that membership predicate with
element-for-element equality of the raw `/proc/PPID/cmdline` NUL split against
the expected 29 byte strings plus the single trailing empty string. It rejects
missing/extra NULs, empty extra arguments, reordered flags and numeric spellings
such as `10.0`, rather than normalizing them. The operation is still restricted
to exactly `hybrid` or `alarm`.

The expected vector is independently checked against the literal registration:
`/usr/bin/python3 -I -B ROOT/run_capped.py`, wall10, CPU10, RSS536870912,
RSS sample0.05, termination grace0.25, exact ROOT cwd, operation-specific
ENG stdout/stderr/telemetry, separator `--`, and the complete
`/usr/bin/python3 -I -B ROOT/engine.py OP ENG/OP.authority.json` child tail.
ROOT remains `/home/ubuntu/d125-hybrid81-exact-solver-20260907`,
ENG its `engineering` child. The outer registered `prlimit` prefix execs the
Python parent and therefore is not part of that parent's observed argv.

An exact byte-restoration control removes the new function and restores the
one old predicate, recovering the frozen original helper byte-for-byte.
Thus all other binding, timer, deadline, limits, paths, script/checker logic,
exclusive writes and same-PID exec are unchanged. `driver.py`, `exact.py`, and
`hybrid.py` are copied byte-identically with their original pins; notably the
generic driver's own parent check is not changed or newly authorized here.
`original_engine.py`, registration, and `parent-argv.patch` preserve the delta.

## Actual bounded controls

The self-contained `check.py` uses the actual old/new `payload` functions,
mocking context, file hashes, PID/PGID, cwd, output absence and raw parent bytes.
A sentinel replaces `D.arm_deadline`: valid input reaches its call with the
unchanged duration7 for hybrid or1 for alarm, before setting a timer. Limits,
writes and exec are forbidden sentinels. Every invalid input rejects at the
new parent predicate, before the deadline or any payload write. No authority
file exists in these tests; the context dictionary is explicitly mocked.

Each normal/optimized run passes94 labeled payload cases: both valid operations;
changed values at each of29 positions per operation (including both Python
interpreters/flags, runner, caps, all output paths and complete child tail);
nine missing option values; extra/missing arguments, NUL errors, reordered
flags and a nonliteral numeric value; plus each operation's changed wall/output
object that reaches the OLD sentinel but is rejected by the NEW helper.
The helper, checker and dependency ASTs contain zero `Assert` nodes. Controls
also pin D/E/H and reconstruct both vectors directly from registration.

Retained normal/optimized stdout is byte-identical, stderr empty, both rc0:
0.231624s and0.552780s external elapsed (0.784404s combined). Each child used
timeout30s, CPU25s, AS512MiB, FSIZE64MiB, core0 and Python `-I -B`, plus `-O`
in the optimized run. `replay.json` records exact commands and hashes.
Replay from the owned box or a flat corpus containing its declared modules:
`/usr/bin/python3 -I -B check.py` and
`/usr/bin/python3 -I -B -O check.py`, under those same external caps.
No old fixture/test sibling is needed. These are mocked dispatch controls,
not live runner acceptance or same-UID adversarial isolation.

## Unchanged live requirements and custody

Actual Singular remains GAP. Root must separately authorize and establish the
registered retained-instance/EBS, fresh host/boot/process/resource and exclusive
output custody; physical helper/D/E/H/fixture/CAPRUN/Singular/GREEN pins; two
distinct operation-bound authorities; and generated plus promptly captured
live complete-command equality, PID/PGID/start/namespace/cgroup/cap agreement.
Exactly one hybrid must terminate normally rc0 with empty stderr, complete
seven-slot I/T output, I_SIZE4, G=[1], the prescribed duplicate map and direct
lift; the retained streams need normal/-O exact replay. Only after its terminal
acceptance may exactly one alarm reach the ready marker and terminate by actual
SIGALRM14 at the inherited one-shot deadline, before the external10s fail-safe.
Timeout, parse failure, wrong signal/return, missing marker, or slot drift fail.
Telemetry-first retention, exact pre/post pins, all-group terminal absence and
root STOP remain mandatory; no retry, cap enlargement or production phase.

The <=5-minute independent delta-review prompt is prepared at
`box/d125-hybrid81-parent-repair-20260907/delta-review.prompt.md`, with unique
charged basenames and `{{LANE_INPUTS}}`; it has NOT been launched. No runner or
framework was added. Input/owned hashes are in the adjacent `custody.json`;
publication uses begin/close/finalize/verify. All tests and artifact writers are
terminal at handoff; original files remain immutable. STOP/IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5682`.
- Body SHA-256:
  `b6e555e8c7523271588a1c4db8a0b0365d3473397767433257653bea2e9ceeda`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
