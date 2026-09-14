# f10 mixed LoadState correction gate

Status: **CONDITIONALLY STATIC CONFIRMED** for the corrected unit and unchanged PREPARE. No runtime, worker, or scientific authority follows.

First action: `2026-09-13T00:45:39.742144236Z`. All eight charged pins matched before use. Six current bodies were read WHOLE; unchanged policy/finalizer WHOLE reads were reused after exact repinning.

## Corrected unit delta — CONFIRMED

The complete delta from unit SHA `96258465fbc33d403072ad540bea782e4abf29092c4f5617a0c56043d3025b48` is confined to post-wait state classification and the reset/GC race:

- `systemctl show` must return zero, and its retained property file supplies the single exact `LoadState` value;
- `loaded` preserves the pre-reset cgroup-procs byte check and no-child-directory check. If `reset-failed` loses a garbage-collection race, a fresh exact query must say `not-found`; expected kernel cgroup absence is still mandatory;
- `not-found` is the only alternate state. It requires the separately saved real `systemd-run --wait` code to be zero, a responsive manager, absence from `list-units --all`, and absence of the frozen expected kernel cgroup;
- any other/empty/multiple state fails exact string comparison. No `ControlGroup` default or blank value is used as evidence, and the final wait-code-zero predicate remains unchanged.

All calendar rendering, original admission/deadline, caps, service argv, source pins, layout, journal/late capture, cgroup cleanup, census, transfer obligations, and no-retry boundary are byte-identical. The correction is source-static only; actual systemd output, cgroup state, and timing still must be observed on the registered worker.

## PREPARE reconsideration — CONFIRMED WITHDRAWAL

I withdraw the prior report's claim that PREPARE's unconditional post-wait `systemctl show` would abort merely because a successful transient unit had unloaded. The supplied exact evidence records exit `0` and a nonempty seven-property result for an absent unit on systemd 255, with `LoadState=not-found`, `ActiveState=inactive`, and `SubState=dead`. ROOT independently repeated that exact read-only query with the same result.

PREPARE saves the real `systemd-run --wait` return code before `show` and explicitly requires it to be zero afterward. It does not derive success from the default `Result=success` or `ExecMainStatus=0` fields. Therefore an unloaded successful service does not trigger the alleged abort, and those defaults cannot turn a failed real wait into success.

Within the previously charged PREPARE scope, the source remains conditionally static-sound: placeholder-disabled; fixed source checks; global TERM/KILL armed before the first metadata service; stated per-service caps and interpreter flags; actual independent string-only facts; unchanged assembler/inventory bounds; explicit real wait checks; and no dummy/science launch or qualification-success claim. Its terminal property files must be interpreted as documentary state, not proof that an absent unit executed. Fresh live controls, cgroup/cutoff evidence, receipts, physical/native fit, custody, and durable transfer remain ROOT obligations.

No source was edited or executed. No systemd job, interpreter, import, dummy, science, worker, or AWS action occurred.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3305`.
- Body SHA-256:
  `8d39bd74f090c5633445a9500a624dc9d87f5354554615ef0958a7573d102a5e`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
