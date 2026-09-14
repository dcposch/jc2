# Supplied-input candidate emitter — provisional pending FIRST

## Interface

`python3 -I -S -B caller.py PREPARED_DIR PREPARED_PINS_JSON OBSERVATION_JSON DECISION_JSON PREFIX EXPECTED_CONTEXT`

Exactly six arguments. Expected context is explicitly `HISTORICAL_TEST` or `ROOT_ATTESTED_CANDIDATE`; it must equal the supplied observation, decision, candidate SUMMARY, and patch packet contexts. The directory supplies exactly the four fixed prepared basenames required by the accepted binder. Expected prepared pins and the decision/observation are supplied by ROOT, not synthesized by the caller. The historical fixtures are tests only, not current authority.

The two-entry `DEPENDENCY_PATHS` binding is location-only. A flat immutable reviewer can replace it in memory before calling `main(argv)`, retaining both literal `DEPENDENCY_SHA256` values. Both helpers are bounded-read and hash-checked before either import. ROOT guarantees trusted immutable paths and absence of concurrent replacement; no adversarial filesystem authentication is claimed. Imports disable bytecode writes.

## Processing and output

Reads are bounded to 131,072 bytes each, including the three metadata JSON inputs. The parents retain their 131,072-byte per-candidate and 524,288-byte aggregate limits, strict UTF-8, CR/NUL, LF, JSON duplicate/nonfinite/fractional-number, schema, and binding checks. All metadata JSON is parsed through `latebind.load`. Then `bind` produces the fourteen candidate byte strings only in memory.

Before `make_patch`, reject each of U+000B, U+000C, U+001C, U+001D, U+001E, U+0085, U+2028, and U+2029 anywhere in candidate text. This adds the universal-newline transport restriction; it does not replace parent validation. The result preserves exactly `patch`, `expected_sha256`, `status`, `context`, and `candidate_bytes`, including all fourteen hashes and complete SUMMARY as patch content. Serialization is ASCII JSON with one final LF, fully constructed and bounded to 8 MiB before stdout. This serialization envelope is not a worker budget or a new execution limit.

Success: exit 0, one complete JSON object, empty stderr, candidate-only status `CANDIDATE_NOT_INSTALLED_NOT_RELEASED`. Validation/input/dependency failure: exit 2, empty stdout, exact stderr `REFUSED: candidate input or dependency\n`. Output-device failure itself is not represented as successful complete emission; no atomicity of a pipe or terminal is claimed. Nothing is applied, installed, observed, released, or written as a candidate.

## Qualification and boundaries

The explicit standalone historical test launches only this own short stdlib caller, with a ten-second timeout. The six test methods additionally exercise `main(argv)` in memory. The fixture/output location bindings in `test_caller.py` may be replaced in memory for a flat review snapshot, preserving frozen historical/helper hashes. The standalone subprocess uses the installed sibling helper locations; location-only external replay can instead call the same `main(argv)` after rebinding. No dependency search or plugin mechanism exists.

Independent LF patch readback reconstructs all fourteen byte strings in memory and compares all EXERCISE hashes, four complete historical final documents, 78,889 candidate bytes, SUMMARY context and no-release flag. The ASCII stream test includes the historical em dash. Eight nonvacuous separator cases rebuild prepared and decision commitments and first succeed through both parent APIs; only the new caller's hygiene barrier refuses. Other cases cover missing argument/file, bad pins/context/decision, malformed JSON, and helper hash refusal before imports. Test scripts create no fixture or candidate files.

ROOT still authenticates current helper/caller/input pins, physical facts, clocks, approvals, the opaque native-list digest's correct role, complete prepared text, private absent output prefix, symlinks, concurrency, and any later application/readback. The inherited uppercase-placeholder restriction is not a comprehensive template audit. Add File transport is not exclusive filesystem creation. The caller neither guarantees full 120-second deployment feasibility nor executes an installer, source, probe, dummy, holder, shell payload, worker, or timer. FIRST independent review is required before operational use.

## Quantity / cheapest test / collisions

Quantity: six completed documentary test methods, including eight separately committed forbidden-separator subcases; fourteen historical candidate objects remain in memory. Cheapest meaningful test is the real historical CLI plus full in-memory LF/hash readback, planning wall 10 seconds (bounded test timeout, not deployment prediction). No new canonical OPEN ID. Remaining deployment facts belong to ROOT's existing boundaries, not an added code gate or a new helper framework.
