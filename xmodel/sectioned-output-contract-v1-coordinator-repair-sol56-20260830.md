# Coordinator repair: `SECTIONED-INDEPENDENT-CALLS/v1`

Coordinator: Sol 5.6 Ultra  
Date: 2026-08-30 UTC  
Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`  
Lifecycle: **REPAIRED / RE-REVIEW REQUIRED / NOT ENABLED IN ANY CALLER**

## 1. Review custody and disposition

Opus hostile review closed `DONE`, exit zero, with report SHA-256
`08759757e9241b531b28930c557c7a3b63b90f40511fb919adf4bb1e590219f5`.
Its verdict on the charged prototype was `REPAIR_REQUIRED`. The two mandatory
findings were real: an unhandled `OSError` during post-write input validation
could leave the output behind, and a section body could smuggle reserved
terminator/provenance markers. The tool had and still has no caller, so no
research artifact or mathematical verdict consumed the defective prototype.

The reviewed input hashes were

```text
593bc16465eac0b1146b08b724226cea3b449178090d974dbdfb0357d40f5473
  ops/sectioned_output.py
b8e311fe915b2589ab13307840bed4b3e2864d6d13fe1976b65db8f9c9bb30a1
  ops/test_sectioned_output.py
```

The repaired hashes are

```text
748684b1e922763f23b84a12b76b0ccc773b245fb1cafa943532166722c2cf64
  ops/sectioned_output.py
de27eaadb62989ebb5a70e2add4d573d91c51f8c9ae7b5cc489f3677c7b58184
  ops/test_sectioned_output.py
```

## 2. Binding repairs

1. Every final-file read now opens with `O_NOFOLLOW` when available, checks
   the pre-open and opened identities, reads from that descriptor, checks a
   full metadata snapshot, and rechecks the path identity. All filesystem
   errors become `ContractError`. Section presence uses `lstat` and treats
   only `FileNotFoundError` as absence.
2. Section bodies reserve the substrings `BODY-END`, `SECTION-END`, and
   `<!-- SECTION `. Leading whitespace, mid-line placement, and forged
   provenance therefore fail before assembly.
3. Exclusive output creation converts every `OSError` to the documented
   contract failure. Write failures attempt exact-path quarantine; a cleanup
   failure is itself reported rather than hidden. The post-write validation
   guard catches both contract and operating-system errors and removes the
   output before returning failure.
4. Manifest paths reject control characters before `Path` operations.
   Parent inspection distinguishes absence from permission and I/O errors.
5. JSON object construction rejects duplicate keys. The prototype no longer
   claims to enforce a canonical JSON serialization that it does not check.
6. The manifest and receipts now call the prompt digest
   `prompt_sha256_declared`. It is explicitly an unverified operator
   annotation, not evidence that any prompt file was read.
7. The documentation no longer claims immutable sections or existing
   `ops/lane.sh` wiring. It states the exact 0/2/4 exit meanings and that the
   total-file budget includes the terminal marker.

These address review findings R1--R9. The tool remains an opt-in byte-contract
experiment, not a provider runner, authentication layer, semantic checker, or
proof system. No green receipt is evidence for the truth of assembled prose.

## 3. Verification

The focused suite passes 9/9 under ordinary Python, `-O`, and `-OO`. New
fixtures cover reserved-marker smuggling, duplicate JSON keys, control bytes
in paths, and non-`FileExistsError` output-creation failure with no traceback.
Byte compilation passes. The complete `ops/test_*.py` suite passes 47/47 under
ordinary and optimized Python.

Because the review charged earlier bytes, these repairs do not inherit its
approval. A stable-basis hostile re-review is required before any caller or
promotion path is wired. Until then the lifecycle is `TRIAL_NOT_ENABLED`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3659`.
- Body SHA-256:
  `e45631047f915f9e65fb92b1494634d84d948fc79ca3ead8091a4ee0fe077219`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
