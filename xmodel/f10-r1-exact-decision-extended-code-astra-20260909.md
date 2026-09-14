# F10 r1 extended exact-decision code — preparation only

Basis 0d39df3c9fd69c939a8420c54d03228b9077777d. First action 2026-09-09 15:16:26 UTC; controlling stop 15:28:26 UTC. Status: COMPLETE CODE PREPARATION, UNEXECUTED, PENDING DELTA REVIEW. No retry, worker, dispatch or ideal-decision authority is created.

## Exact changes

The two new copies are in box/f10-r1-exact-decision-extended-code-astra-20260909/. Their originals remain unchanged. caller.py SHA256 **386a352d654fb72a81026dc39a2a13aeb72020d69f5c11b0b10e8d01a099523b** differs from c52a2f4cdbfe477b97f7cef2c162df3d73a1a221ebc32825acaf9aa2ad62c943 at only three executable sites:

- Aggregate mathematical ceiling: first_math + 120 becomes first_math + 690 seconds.
- Engine stage: 60 wall / 50 CPU becomes 600 wall / 550 CPU seconds.
- Verifier stage: 30 wall / 25 CPU becomes 60 wall / 50 CPU seconds.

Semantic validation remains 30 wall / 25 CPU. Default 2 GiB sampled RSS, 16 MiB per-file limit, exact argv/source/host guards, fresh same-caller controls, sequential children, +15-second admission margin, stored root deadlines, post-return cutoff check, strict cap/failure refusal and all other bytes remain unchanged. The existing semantic validation receipt is still required in decide mode with the identical checker/test hashes; no semantic rerun requirement or bypass was added.

engine.py SHA256 **6123faf96ab70abcd1d00f545619eaa9c64145c621035d7c8f37be801cf09d4b** is based on the corrected 81e52951192afbbcbfcd7c11ef604ec45a470ca35a93afec2c8416dac985a5d1. Its only changes are importing resource, collecting resource.getrusage(resource.RUSAGE_CHILDREN) immediately after child.wait(), adding the returned accounting metadata to the existing receipt, assigning ENGINE-FAILED-INCONCLUSIVE when the signed nested returncode is nonzero, and moving the unchanged rc/hash acceptance check after the exclusive receipt write.

Thus a normally reached wait returning nonzero now preserves the actual signed Popen returncode before the same refusal raises. Negative signal returncodes are not converted to unsigned exit numbers. The existing receipt remains CANDIDATE-ONLY-NOT-DECISION for rc=0; this is not acceptance, and the unchanged hash check still runs afterward. A hash mismatch still raises. There is no exception overhaul: an earlier identity failure, wrapper death, failed hash read or failed receipt write may still prevent this receipt. The change does not promise crash-proof logging.

children_rusage records user_cpu_seconds, system_cpu_seconds and maxrss_kib. These are operating-system metadata, not polynomial coefficients or exact rational witnesses. RUSAGE_CHILDREN is cumulative accounting for children waited for by this wrapper, not wrapper-self accounting, per-PID attestation or a sampled live process-group measurement. On the intended Linux platform maxrss is in KiB and is the largest child high-water mark, not an aggregate PGID RSS sum. Descendant accounting is limited by the operating system's child/wait accounting. These fields do not replace CAPRUN measurements or resource classification. No new process group, inner supervisor, flags, source transformation, optional integer-limit change, extra cross-check or checker change was introduced.

The complete literal diffs are caller.diff SHA256 a8b751c2b7a77d6fcf56dd810a790595051ea66a2d0862908ea242bad9ad8091 and engine.diff SHA256 73ab3a75b7937ebae46144f3ae35c1fa3601e1686199bfbf5ac8bde3d0881f25. Each saved diff was byte-compared with fresh git diff output. The full new sources were read statically; no source was compiled, imported or run.

## Retained first-attempt evidence and uncertainty

The six permitted inputs were hashed before whole reads. Old engine.telemetry.json ca1b8770... reports NORMAL_EXIT, wrapper returncode 1, resource null, wall_elapsed_seconds 51.59926408 and sampled peak group RSS 139493376 bytes. Old engine.stderr b1215e53... identifies the wrapper's combined nonzero-rc-or-changed-engine refusal before receipt construction. These bytes do not reveal the nested returncode or prove a CPU timeout. A CPU-limit explanation is only an inference; no typed CPU cap is asserted. Low measured RSS in that one run is not a forecast for a longer run.

Root reports that the actual transcript contained twenty row blocks but no BRANCH/DONE and no verifier ran. The transcript was not an allowed input here, so that is retained as root-supplied context, not a new independent transcript verification. The first attempt remains INCONCLUSIVE. Accepted static code and runtime-validation gates were read whole at their qualified scopes; their provenance artifacts, actual ideal and theorem interiors were not opened or replayed.

## Pending and handoff

This prepares one separately reviewed same-representation attempt. Q, the twelve-variable order, all twenty slots, std/lift choice, output protocol, certificate semantics and exact artifact binding are unchanged. There is no prime/order/RAM/presentation farm or automatic escalation. The longer caps do not enable the caller without a fresh root registration, clocks, pinned sources and worker authority. Existing CAPRUN sampling and cleanup overshoot limitations remain; a cap, mismatch or late return still yields INCONCLUSIVE.

New-source executions and tests in this task: zero. Only apply_patch edits, documentary reads/diffs/hashes and publication tooling ran. No AWS/SSH/network/worker action, mathematical subprocess, compilation/import or test occurred. The next required step is the single root-owned narrow Fable code/cap delta review, followed only if separately authorized by fresh same-caller controls in a new registered run. Checker/tests remain untouched; this report does not request another semantic replay.

READ-SCOPE.md and input-pins.json record the exact six inputs and read boundaries. All originals and owned files are pinned in custody. Own source/report whole-read and own-only raised-item check preceded sealing; no new open mathematical item or collision is raised. All writers are idle at terminal handoff.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6082`.
- Body SHA-256:
  `1028d976491c90dbe3d82efe7dbe1e8e403b49b7013b32d65d70484fce69db88`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
