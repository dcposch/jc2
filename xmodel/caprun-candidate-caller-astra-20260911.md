# Supplied-input metadata candidate caller

Status: COMPLETED documentary implementation and historical qualification; PROVISIONAL pending FIRST review. No operational authority.

First action: 2026-09-11 18:14:45.934094826 UTC. Original publication reserve 18:32 UTC; hard stop 18:35 UTC. Basis: 0d39df3c9fd69c939a8420c54d03228b9077777d.

## Outcome

The small six-argument caller composes the two accepted immutable helpers without changing them. It consumes supplied prepared bytes, expected pins, observation and ROOT metadata decision, explicitly requires the requested context, rejects all eight forbidden universal-newline separators before patch construction, and emits only an unapplied ASCII JSON packet. It does not observe or authenticate a host, install files, run an input, or release anything.

The real standalone `HISTORICAL_TEST` CLI passed. Its fourteen output hashes exactly match the frozen EXERCISE, with 78,889 candidate bytes, candidate-only status, and complete SUMMARY context/pairing. Independent LF patch readback reproduced all fourteen byte strings in memory and compared the four historical final documents byte-for-byte. No candidate outputs were written or applied.

## Implementation and interface

Owned source: `box/caprun-candidate-caller-astra-20260911/caller.py`; tests: `test_caller.py`; full interface/read-scope: `CONTRACT.md` and `PINS.json`.

Invocation: `python3 -I -S -B caller.py PREPARED_DIR PREPARED_PINS_JSON OBSERVATION_JSON DECISION_JSON PREFIX EXPECTED_CONTEXT`. The contexts are exactly the inherited `HISTORICAL_TEST` and `ROOT_ATTESTED_CANDIDATE`, never guessed. `DEPENDENCY_PATHS` is a two-entry location binding for immutable flat-review relocation, with independent fixed hashes still enforced before either import. Reviewers can supply relocated fixture paths and call `main(argv)`; this is not a general discovery facility. Bytecode writes are disabled for helper imports.

Success is one fully serialized ASCII JSON object with the parent's five fields and all fourteen hashes. A validation/input/dependency error returns 2 with empty stdout and exact stderr `REFUSED: candidate input or dependency\n`. The complete packet is bounded before output; output-device atomicity is not claimed. File reads remain individually bounded to 131,072 bytes. Parent candidate limits remain unchanged; the 8 MiB escaped packet envelope is a serialization bound, not a worker cap.

## Actual documentary tests

The authorized command was `python3 -I -S -B box/caprun-candidate-caller-astra-20260911/test_caller.py`. It launches only this own short stdlib caller, with the supplied three owned historical JSON fixtures and a ten-second subprocess timeout. An initial run passed six test methods in 0.255 seconds; after the read-only bytecode setting, the final-source run again passed all six in 0.256 seconds. These are observed unittest durations, not a full deployment measurement or a 120-second feasibility claim.

The six methods cover standalone CLI success; an ASCII-only stdout stream including historical em-dash content; missing argument/file refusal; bad prepared pins, mismatched context, false decision and strict-JSON negatives; dependency hash failure before either helper import; and eight individually checked forbidden separators. Each separator case updates the prepared and decision commitments and first succeeds through both accepted parent APIs. The caller then fails specifically at its new hygiene barrier, with empty stdout. These are genuine controls, not stale-hash failures. The test harness independently reconstructs fourteen files from the patch using literal LF semantics and hashes them in memory.

Exactly three additional fixture inputs were authored, all historical: `fixture-pins.json`, `fixture-observation.json`, and `fixture-decision.json`. Historical identities, approvals and the old prefix are never current authority; the prefix is treated as a string, not opened or written. No scientific/runtime/native/source/dummy execution, input-shell execution, worker, AWS/SSH/network, process inspection/control, or patch application occurred. Only the explicitly authorized documentary caller/tests and ordinary publication metadata ran.

## Scope, custody and remaining boundary

All sixteen charged inputs (179,304 bytes) were freshly pinned before fresh human WHOLE reads. These comprise TASK, seven helper/test/review/exercise texts, and eight historical files. The large final registration read clipped a narrow region; separate lines 230–350 recovered it before implementation. No summaries were substituted for required whole reads, and no linked sources were traversed. The tests later read the same pinned historical byte files, two helper sources and EXERCISE. Current postpins at 18:24:15 UTC matched all sixteen originals. Own sources, fixtures, contract, pins and report receive whole readback before seal; final custody binds all owned outputs except itself.

ROOT still authenticates current input/helper/caller bytes and supplied expected pins, physical/liveness facts, native-list role, clocks, actual approvals, full prepared-text semantics, prefix absence/privacy/symlinks/concurrency, and any later installation/readback. The parent's uppercase placeholder recognition is not a comprehensive audit. Add File is not exclusive creation. No release authority or broad production qualification follows from a historical test. FIRST independent review remains required before operational use.

## Quantity / cheapest test / collisions

Quantity: six documentary methods, eight separately committed separator cases, fourteen in-memory historical outputs. Cheapest discriminating test is the already-run real CLI plus independent whole-byte patch readback; numeric planning bound is 10 seconds for that subprocess, UNMEASURED for future hosts. No new canonical OPEN identifier, framework, mathematical claim, or duplicated foundation review. The only remaining acceptance boundary is the assigned FIRST review and ROOT's existing future operational duties; no follow-on is authorized.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6104`.
- Body SHA-256:
  `f8f6100d265d358cab3f1eef123a8b656982d80cced440603f65180d3d2f53f7`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
