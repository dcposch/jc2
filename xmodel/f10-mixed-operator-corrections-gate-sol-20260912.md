# Focused FIRST: mixed operator corrections

Status: **CONDITIONAL STATIC CONFIRMED / UNEXECUTED / NO AUTHORITY**. First
action `2026-09-12T22:33:10.463892856Z`.

Whole old/new diffs confirm only the declared corrections.

- COMMANDS changes its title, adds exact seven-key `cgroup_controls` census,
  replaces LF-stripping command substitution with a separately materialized
  one-LF expected file plus byte-exact `cmp`, and replaces pseudo-file
  `test ! -s cgroup.procs` with `head -c 1` into a regular evidence file plus
  empty-file check. Existing no-child-directory and post-reset exact cgroup
  absence predicates remain.
- Dispatcher removes only `HOME:str(out)` from the otherwise identical closed
  five-key TMP/TEMP/XDG/PYTHONPYCACHEPREFIX environment. Because `env=` replaces
  rather than extends the inherited environment, HOME becomes absent; no
  inherited variable is newly admitted. All flags, phases, source/authority
  structure, caps, clocks and outputs are byte-identical.

The cgroup correction observes actual returned content: GNU head EOF is a
successful empty read, while inaccessible/read failure aborts under `set -e`.
It proves emptiness only at that instant, appropriately followed by child-dir
and final disappearance checks. The regular evidence byte count is later
included in the same bounded census/hash custody. The `cmp` target contains
exactly one terminating LF, closing the earlier shell-substitution loss. The
nested-key comparison rejects both missing and extra controls.

I find no blocker in this scoped static delta. It does not establish actual
runtime, future quiescence, no escape, native closure, tool semantics or
physical mount/unit ancestry. Fresh actual-host bindings, source hashes,
timers, cgroup evidence, successful predicates, cleanup and durable custody
remain mandatory. No command/source was executed or repaired here.

Fresh WHOLE reads covered all six PINS inputs; final WHOLE readback covers
PINS, report and manifest. Strict postpins precede terminal custody. No AWS,
network, process control, interpreter/import/syntax/AST/dummy/CAS or protected
tree access occurred.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `2155`.
- Body SHA-256:
  `0bb4fd730d923d3a37a238c69c371fe3ce6c96f8cadf74238b14ef6e46f1f618`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
