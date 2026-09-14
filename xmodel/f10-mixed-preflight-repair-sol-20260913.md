# F10 mixed preflight minimal repair — Sol

Status: **MINIMAL STATIC REPAIR COMPLETE / UNEXECUTED / UNREVIEWED**

First action: `2026-09-13T08:03:16.873454093Z`. Original reserve `08:07Z`; hard stop `08:09Z` on 2026-09-13.

## Verdict

The owned derivative changes exactly one expression in the old 97-line preflight:

```diff
- diagnostic.splitlines().count(cause) == 1
+ diagnostic.splitlines().count(cause) >= 1
```

This is the minimal correction for the observed Ubuntu apport behavior. One or more complete lines exactly equal to the selected expected `ValueError: ...` cause now satisfy the cause predicate; zero occurrences still fail. The preflight still requires a nonzero observer exit, absence of verbose-import lines for `sympy` and `flint`, zero-byte stdout, and absence of the job output root for every negative control. It does not accept a substring, a different cause, a successful exit, or an early run that created output.

Every other byte and condition is preserved from pinned source `21e2bb41...c57882`, including HQ/instance/cgroup guards, isolated startup, observer pin, credentials, dependency inventory bounds, exact record creation, and final fsync. Whole static inspection found no second concrete blocker in this narrowly charged source. That statement is source-static only, not an execution result or a general environment assurance.

## Scope and authority

The derivative is inert. It has not been parsed, imported, executed, tested, or run on AWS. It grants no retry, worker, preflight, observer, or scientific authority. ROOT must independently review its exact delta and bind a fresh qualified worker and original clock before any execution. The earlier failed run remains failed and closed.

Inputs and personal read scopes are recorded in `PINS.json`; strict postpins are required at closure.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `1854`.
- Body SHA-256:
  `07db61c80d25bf21d9abdb241ba77912a3bac03ac10a8965615e0f114be16a6c`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
