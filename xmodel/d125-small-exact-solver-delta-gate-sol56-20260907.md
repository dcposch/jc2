# D125 exact-stream two-check delta gate

Status: **CONFIRMED for repaired literal-stderr and size/index semantics only.** Independent narrow review of the frozen repaired parser and pinned actual control only.

## Scope

All five frozen inputs in `/tmp/jc2-lane.9HIsyw/inputs` were read in full. This gate is limited to repaired literal-stderr and `I_SIZE`/indexed-nonzero semantics; it does not repeat or authorize solver arithmetic, certificate criteria, source/serializer, caller, engineering controls, full-source streams, deployment, or solving.

The charged repaired `exact.py`, patch, and actual `control.stdout` have SHA-256 values `7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9`, `1cccb1738f7d27cf20ea181099c4105baa434189786703480e538164edf39b3e`, and `fff5dfd6b2be427844ea898b95c8e159937761085ec2905b0327dc6871939922`, matching the frozen repair record. Inspection found the two advertised executable changes: literal `stderr == b''` and equality between `I_SIZE` and `sum(bool(row) for row in engine)`.

## Delta decisions

| check | decision | independent concrete result |
|---|---|---|
| repaired literal-stderr semantics | **CONFIRMED** | The pinned actual stdout was accepted with `b''`; the same bytes with stderr `b" \n\t"` were rejected as `nonempty stderr`. |
| repaired size/index semantics | **CONFIRMED** | The unchanged actual `I_SIZE 3` stream was accepted as six indexed `I` rows with exactly nonzero positions 2, 4, and 5. Positions 2 and 4 are equal nonzero `x` rows and were counted separately. Exact single replacements `I_SIZE 3` to `0` and to in-range upward corruption `4` were each rejected as `engine size/nonzero count mismatch`. The six indexed `T` rows remained present. |

A separate parser-only fixture with three indexed zero `I` rows and `I_SIZE 0` was accepted. This establishes the zero-count edge of the stream invariant only. The checker deliberately invoked no unit or properness certificate function for that fixture, so parser acceptance is not presented as a certificate verdict.

## Reproduction and limits

Own evidence is confined to `box/d125-small-exact-solver-delta-gate-sol56-20260907/`. The stdlib checker `gate_check.py` accepts `--inputs PATH`, uses explicit exceptions, and statically found zero `Assert` nodes in itself and the charged `exact.py`. It ran against the frozen directory with `python3 -B` and `python3 -B -O`; both recorded all five expected outcomes in `normal.json` and `optimized.json`. Their SHA-256 values are `d20074ae10e1345c3c25f818672401d0999cb8e1339fc73276b900628c317dd4` and `505aca884d56b85c89bd62ce49b383e124b51795210d64d8a3b0925128406864`; the checker hash is `eac03263a4c28d3cd5325e81bc208aaed1732e100595e0d7b42de899cd97e942`.

Each command was bounded by a 30-second wall timeout, 25-second CPU limit, and 512 MiB virtual-memory limit. The normal run used 0.05 seconds wall, 0.04 seconds child CPU, and 20,048 KiB peak RSS; the `-O` run used 0.17 seconds wall, 0.17 seconds child CPU, and 22,792 KiB peak RSS.

No CAS, AWS, SSH, full-source arithmetic, new lane, live peer material, frozen-input edit, deployment, or solver action occurred. ROOT owns any later deployment or solver authorization; this gate supplies neither.
<!-- BODY-END -->
