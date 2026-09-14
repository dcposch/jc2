# F10 mixed native limits-padding correction

Status: **SOURCE DELTA COMPLETE, UNEXECUTED, UNREVIEWED**. Corrected observer SHA-256: `40bd1116e4cb1bfbfc684afe1d0b0a334af10ed0b719f528efa4ee4a41b483d9` (187 lines, 8995 bytes). No worker, runtime qualification, retry, or scientific authority follows.

First action: `2026-09-13T01:37:01.395186381Z`. All four inputs matched before use; the old observer, ROOT intake, and V4 result were read WHOLE.

## Exact delta and finding

The derivative preserves every old byte except the two `/proc/PID/limits` regex suffixes:

```diff
-...4194304[[:space:]]+4194304[[:space:]]+bytes$'
+...4194304[[:space:]]+4194304[[:space:]]+bytes[[:blank:]]*$'
-...1073741824[[:space:]]+1073741824[[:space:]]+bytes$'
+...1073741824[[:space:]]+1073741824[[:space:]]+bytes[[:blank:]]*$'
```

This admits only horizontal blank padding after the exact `bytes` unit, matching Linux's padded units field. It does not change the required soft value, hard value, unit, start anchor, or line-end anchor. Thus wrong values, a wrong unit, and nonblank suffixes still fail.

V4's observer did exit 1 with empty streams during the live native interval, but its first failed predicate is unknowable from that output design. The formatter mismatch is definite; it is not asserted to be the exclusive historical failure cause.

## Authorized tiny fixture

Run with `LC_ALL=C`; inputs and grep exit codes were:

```text
label=file_valid input=Max\ file\ size\ \ \ \ \ \ \ \ 4194304\ \ \ \ \ \ \ \ \ \ \ \ \ \ 4194304\ \ \ \ \ \ \ \ \ \ \ \ \ \ bytes\ \ \ \ \  rc=0
label=address_valid input=Max\ address\ space\ \ \ \ 1073741824\ \ \ \ \ \ \ \ \ \ 1073741824\ \ \ \ \ \ \ \ \ \ bytes\ \ \ \ \  rc=0
label=wrong_soft input=Max\ file\ size\ \ \ \ \ \ \ \ 4194303\ \ \ \ \ \ \ \ \ \ \ \ \ \ 4194304\ \ \ \ \ \ \ \ \ \ \ \ \ \ bytes\ \ \ \ \  rc=1
label=wrong_hard input=Max\ file\ size\ \ \ \ \ \ \ \ 4194304\ \ \ \ \ \ \ \ \ \ \ \ \ \ 4194303\ \ \ \ \ \ \ \ \ \ \ \ \ \ bytes\ \ \ \ \  rc=1
label=wrong_unit input=Max\ file\ size\ \ \ \ \ \ \ \ 4194304\ \ \ \ \ \ \ \ \ \ \ \ \ \ 4194304\ \ \ \ \ \ \ \ \ \ \ \ \ \ kbytes\ \ \ \ \  rc=1
label=trailing_junk input=Max\ file\ size\ \ \ \ \ \ \ \ 4194304\ \ \ \ \ \ \ \ \ \ \ \ \ \ 4194304\ \ \ \ \ \ \ \ \ \ \ \ \ \ bytes\ \ \ \ \ junk rc=1
```

The two valid padded rows are accepted; all four negative controls are rejected. These were isolated shell/grep string fixtures only—not execution, parsing, syntax checking, or mocking of the observer or a service.

The accepted ROOT qualifications remain unchanged: actual binding must set `LC_ALL=C`; sixty iterations are not themselves a hard 60-second tree cap; timeout is STOP; cmdline has its separately qualified post-argument bound; line feeds are normalized in semantic captures; and future ROOT review plus actual physical/runtime checks remain mandatory.

No frozen input, shared source, cap, phase, authority, controller, or scientific code was changed. No AWS, worker, service, observer, source interpreter, import, AST, syntax, dummy, CAS, or scientific execution occurred.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3109`.
- Body SHA-256:
  `1fbcba1c0f823a38fb6c00992b73c1c0a7e2e0804fab36672a12c2938fcfe801`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
