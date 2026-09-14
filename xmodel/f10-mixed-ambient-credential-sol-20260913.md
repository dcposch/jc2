# F10 mixed ambient-credential candidate — Sol

## Verdict

**CONDITIONAL STATIC CONFIRMED.** The proposed ambient-capability setting is a sufficient capability-side prerequisite for the existing root service → Python/CAPRUN → util-linux `setpriv` → UID/GID 65534 chain. It adds no capability outside the already selected bounding set. It does not establish the cause of V5, defeat an LSM/seccomp denial, prove installed systemd behavior, or authorize a rerun.

Two inert derivatives are delivered. Each differs from its charged parent at exactly one line: the empty `AmbientCapabilities=` assignment becomes `AmbientCapabilities=CAP_DAC_OVERRIDE CAP_KILL CAP_SETUID CAP_SETGID`. No dispatcher, argv, cap, timer, telemetry, predicate, placeholder, or enabled state changed.

## Static credential trace

1. systemd v255 defines `AmbientCapabilities=` as capabilities added to the executed process's ambient set and automatically augments the inheritable set as needed. Linux requires every ambient capability to be present in both permitted and inheritable sets. On exec of an ordinary nonprivileged file, ambient capabilities are preserved and added to the new permitted and effective sets. `NoNewPrivileges=yes` does not erase already-held ambient capabilities; it blocks privilege acquisition through exec.
2. Therefore the root Python process, CAPRUN Python process, and setpriv executable can carry these four capabilities in permitted/inheritable/ambient and receive them effective after each ordinary-file exec, subject to actual installed-file and systemd qualification. `CAP_SETUID` and `CAP_SETGID` are then available for the exact credential changes. `CAP_DAC_OVERRIDE` and `CAP_KILL` are preserved because existing supervision/authority handling already selected them; the derivative does not broaden the bounding vector.
3. util-linux v2.39.3 does not use `capng_change_id` here. It sets NNP, requests `PR_SET_KEEPCAPS`, reads the process capability state, makes already-permitted SETPCAP/SETUID/SETGID effective where available, applies it, calls `setresuid`, reapplies its stored capability state, then calls `setresgid` and clears supplementary groups. Its SETPCAP bump is conditional on SETPCAP already being permitted; this candidate neither grants nor needs CAP_SETPCAP.
4. Linux's UID transition rule clears ambient capabilities when all real/effective/saved UIDs change from a state containing UID 0 to all-nonzero. `PR_SET_KEEPCAPS` preserves permitted capabilities across that transition but does not preserve effective capabilities or the ambient set. setpriv's explicit reapply supplies the short SETGID/groups transition window from its still-permitted set.
5. The final exec of ordinary, unprivileged Python occurs with nonzero UIDs and ambient zero. With no file capabilities, the exec transformation yields zero permitted and effective capabilities; KEEP_CAPS is cleared on exec. The existing probe's exact `CapEff=0` requirement remains the runtime check of that conclusion.

This route necessarily activates the already-bounded four capabilities in CAPRUN and setpriv until the credential drop completes. That is a real privilege-state change, not mere wording, and requires the stated different-model source review plus live identity/capability evidence.

## Exact delta

Both parents contain:

```text
-p 'CapabilityBoundingSet=CAP_DAC_OVERRIDE CAP_KILL CAP_SETUID CAP_SETGID' -p AmbientCapabilities= \
```

Both derivatives contain:

```text
-p 'CapabilityBoundingSet=CAP_DAC_OVERRIDE CAP_KILL CAP_SETUID CAP_SETGID' -p 'AmbientCapabilities=CAP_DAC_OVERRIDE CAP_KILL CAP_SETUID CAP_SETGID' \
```

Parents and derivatives:

- dummy commands: `7809c8ae3733d5e765cec4d5018e57dc4b90d30422dbef66f1f89882fee8cd70` → `98260cfd0ce468aca393128a2deb86cb162bc1c1cbe75591bdebb17c4669dbea`
- science unit: `338e45cef2e50e5bdedf25618bcd4ede02bba0f1c26f9faea8b0762ef064b788` → `783a33f13d0286165c7279c6556a1a1681bab9a9dc4dbcbc9093710050d841c0`

Literal unified diffs were inspected and contain exactly those two one-line replacements.

## Required future observations

Before any use, ROOT still must bind and authenticate fresh host/boot/unit/source/native facts; confirm the installed files are ordinary nonprivileged executables; capture the root chain's actual `CapInh`, `CapPrm`, `CapEff`, and `CapAmb` before the short-lived setpriv transition if the qualification requires attributing V5; require genuine setresuid/setresgid success; and verify final UID/GID/groups, NNP, zero `CapEff` (and preferably zero permitted/ambient), cgroup controls, telemetry, cleanup, clocks, and all existing negative/receipt predicates. Any LSM, seccomp, user-namespace, systemd-property, or physical-file mismatch is STOP.

V5 established only that setpriv's direct `setresuid` returned `EPERM`. Because no live capability or syscall-policy evidence was captured, this report does not retroactively claim that an empty ambient set was the exclusive cause.

## Primary-source basis

- systemd v255 `systemd.exec.xml`, `AmbientCapabilities=` and `CapabilityBoundingSet=` entries.
- Linux v7.0 `security/commoncap.c`, set-UID and exec credential transitions.
- Linux `capabilities(7)`, ambient invariants, exec calculation, UID-change effects, and KEEP_CAPS semantics.
- util-linux v2.39.3 `sys-utils/setpriv.c`, exact setresuid/setresgid/capability ordering.

All outputs are inert, disabled, unexecuted, and unreviewed. No worker, runtime result, or launch authority is supplied.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5517`.
- Body SHA-256:
  `6cb8d6de544a7f2af6860b995d7dd0d96bdec1b56590767228a995f4d5d2519d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
