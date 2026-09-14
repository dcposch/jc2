# f10 mixed native operator: different-model static FIRST

Status: **BLOCKER**. This is a source-static review only. It grants no execution, worker, native-host, no-escape, or scientific authority.

## Scope and provenance

First action was `2026-09-12T22:50:23.268363883Z`. I checked all seven charged SHA-256 values before reading every charged body WHOLE. I reused the already-read, exact-pinned immutable `COORDINATION.md` snapshot and did not read mutable canonical coordination state. The exact input list and read scope are in the owned `PINS.json`.

The intended source delta is narrow:

- the collector appends 21 operator executable roots and changes no recursion or numerical cap;
- the inspector replaces only the old concrete instance literal with the disabled `JC2_INSTANCE_PLACEHOLDER`;
- the DELTA's “38-line” description is an incidental typo: both inspected old and new inspector bodies are 33 lines. This does not alter the byte-diff conclusion.

## Decisive completeness blocker

The added executable-root list is incomplete for the corrected dummy commands. `COMMANDS.md` invokes external `cat` in the boot-ID check:

```text
test "$(cat /proc/sys/kernel/random/boot_id)" = "$TASK_BOOT"
```

`cat` is not a Bash builtin, and `/usr/bin/cat` appears in neither the retained collector root list nor the 21 appended roots. Consequently the proposed metadata collection does not attach that operator executable to the native inventory.

This omission is not caught downstream: `native_records.py` checks that its required roots are a subset of the collector records, but its required set does not enumerate every operator command. Thus a manifest can satisfy the assembler while still omitting the executable actually used by `COMMANDS.md`.

Because source repair is outside this task, I do not alter the collector. The exact minimal source-level correction for a subsequent reviewed delta is to add `/usr/bin/cat` as an operator executable root (with its ordinary canonical-target/dependency collection), or else remove the external dependency through a separately reviewed command change. Until then the native-operator completion is not statically complete.

## Remaining static findings

Apart from that blocker, the root-list adaptation is structurally compatible with the assembler:

- all 21 claimed additions are present exactly once;
- the retained canonical-target/ELF-dependency recursion, deduplication, file-count and byte caps are unchanged;
- extra operator records are compatible with the assembler's required-root subset check and its all-files projection;
- actual future-host fit beneath the count/byte caps remains an observation and STOP predicate, not a result of this review;
- each requested executable root must still be shown by actual output as a direct record or alias. The source does not make that physical fact true by assertion.

The other external command names used by the corrected procedure are represented by the retained or appended roots; shell constructs such as `set`, `test`, `printf`, and `true` are builtins. This statement is confined to the charged `COMMANDS.md`, not a general executable-closure claim.

The inspector's WHOLE old/new byte comparison supports the claimed placeholder-only edit. The placeholder keeps it disabled until ROOT supplies the freshly observed instance binding. Its checks remain scoped to the trusted bounded assembler output and actual external resource limits: its `read_bytes` followed by a length check is not a generic read-before-length bound for adversarial input. The inspector performs the documented hashes, package-copy comparison, ownership/mode/ACL ancestry checks, science/runtime/library census, exact `sys.path` comparison, and `ld.so.preload` absence check without importing science. It does not itself prove dynamic import closure, native no-escape, actual-host qualification, or runtime safety.

## Verdict

**BLOCKER:** the proposed collector does not cover the complete executable set of the corrected operator procedure because `/usr/bin/cat` is missing. The inspector portion is conditionally static-sound, but the packet as a whole must not be promoted or used for execution until a distinct source correction receives its own review and ROOT completes all fresh physical bindings and qualifications.

No source was executed or repaired. No worker, clock, instance, path, metadata size, kernel fact, or runtime result was selected or inferred.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4480`.
- Body SHA-256:
  `6359170dd9d258977d1d8f31a8eeb6d85edc722b1658619e65fef3e1aa645fed`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
