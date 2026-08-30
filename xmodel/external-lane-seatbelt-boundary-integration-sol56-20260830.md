# External-lane Seatbelt boundary integration

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra with independent Codex implementation lane  
Frozen basis: `3fa5867cf95892bf90670d237977e3174d2f318e`  
Lifecycle: **SYSTEMS INTEGRATION / LOCALLY VERIFIED / NO MATHEMATICAL CLAIM**

## 1. Threat and disposition

Two external reviewers previously made out-of-mandate observations about the
excluded nested workspace despite prompt instructions.  Prompt compliance is
not a security boundary.  All external-model adapters are now launched by
`ops/lane.sh` beneath the macOS Seatbelt process sandbox.

The generated profile denies `file-read*` and `file-write*` on both the
literal excluded root and every subpath.  The path is constructed lexically;
boundary setup does not resolve or inspect the excluded workspace.  Seatbelt
enforces the rule on the adapter and every descendant process.  A focused
regression proves denial through both a direct pathname and a symlink alias.

The same profile denies model-side writes throughout the private temporary
custody directory.  Original prompt, fallacy appendix, validator snapshot,
composed model prompt, and sandbox profile are mode `0400`.  The adapter can
read the exact composed prompt but cannot chmod, append to, or replace it.
The coordinator process remains outside the sandbox so it can compute
post-run hashes and remove the temporary directory.

The public `.run.v2` receipt is separately denied as an exact write target
inside the model sandbox.  The unsandboxed coordinator alone writes its
initial and terminal records.  Receipts now pin the actual launcher and
generated sandbox-profile hashes and repeat both hashes after execution; any
launcher/profile mutation quarantines the result.

If `/usr/bin/sandbox-exec` is unavailable, the lane fails closed before it
creates a run.  Receipt schema remains version 2.

## 2. Verification

The complete lightweight operations suite passed in all three interpreter
modes:

```text
python3     -m unittest discover -s ops -p 'test_*.py' -v   50/50 PASS
python3 -O  -m unittest discover -s ops -p 'test_*.py' -v   50/50 PASS
python3 -OO -m unittest discover -s ops -p 'test_*.py' -v   50/50 PASS
```

Shell syntax also passed for `ops/lane.sh` and all four registered adapters.
The focused tests establish:

1. byte-exact positive prompt delivery and ordinary report harvesting;
2. model-side chmod/append denial on the composed prompt;
3. direct excluded-tree read and write denial;
4. symlink-alias read and write denial; and
5. model-side receipt overwrite denial with successful coordinator
   finalization; and
6. unchanged prompt, launcher, and sandbox-profile hashes on allowed work.

All fixtures use a temporary fake repository.  No test reads, lists, stats,
builds, modifies, or controls the actual excluded workspace.

## 3. Scope

This is a same-host macOS boundary, not a container or proof of arbitrary
kernel isolation.  It intentionally permits ordinary reads and writes in the
campaign repository because reviewers must inspect frozen evidence and write
their one assigned report.  Existing file descriptors or independently
created hard links are outside the tested pathname threat model; no such
descriptor or link is passed by the lane launcher.  Network access and the
model vendor's own execution environment are unchanged.

The patch proves no mathematics.  Its purpose is to make future independent
reviews less error-prone and to turn an excluded-path instruction into an
enforced local process boundary.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3549`.
- Body SHA-256:
  `101de3a7b210e33f60430532bc48199a81f4609233dc01951508767e9ce6dc2a`.
- Frozen basis: `3fa5867cf95892bf90670d237977e3174d2f318e`.
