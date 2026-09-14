# input_custody — f10-direct-rows-runtime-gate-fable5-20260911

Lane inputs directory: /tmp/jc2-lane.FaRhLi/inputs (13 unique basenames, read-only). Pre-read pins taken 2026-09-11T03:48:46Z with `sha256sum -c` (13 OK, rc=0) BEFORE any body was read. Every file read FRESH_WHOLE through EOF; no clipping; no prior-WHOLE reuse.

| sha256 | basename | lines | bytes |
|---|---|---|---|
| f5b6e6c43da4574c1dd9fc241d2f0596071ab505d561e67579eb28d382814480 | dispatch.py | 661 | 43549 |
| 09845fabff9a8b7f997e3b2d01160e5ff51d728124b9f5cd0b7176f8c19ea063 | probe.py | 186 | 10642 |
| cc0621aa44d17b1dac346e87d20a53f69ce950b343d68c8ed0d3791d42120af0 | mutate.py | 260 | 16196 |
| e2ce5a5f91a61a253e0d355fbb3c982b0968bd2e4bd05a7fcb9eeab95fe402a1 | CONTRACT.md | 53 | 13123 |
| eab97643f515b17716e86f72689a46a1dc73eb9091c1c90b789f690bfa7aeeae | DISABLED-REGISTRATION.json | 134 | 3235 |
| f5f283bc68bfd35cbdc1019c0f7c13f8cd656e47ab11dce9a491552a4c9b3d0f | DISPATCH.diff | 306 | 23684 |
| ee0f1b5b9ec44db883a803df48375e66b79f82e8d35d09e55b4dd62bf6e9b614 | f10-direct-rows-runtime-astra-20260911.md | 48 | 7874 |
| 05775a6f4484e677aff987ef0f203861440721801471fb6f4b20a782cdcbeb11 | f10-source-cone-r3-runtime-gate-fable5-20260911.md | 76 | 24017 |
| 4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2 | run_capped.py | 1198 | 42671 |
| 90c940b021ba9f99f2298aaf394cb082793812ad4428e249b970ecf06baa6c47 | f10-direct-rows-wire-root-20260911.md | 205 | 12558 |
| 2b2770fe494098812a52c6829a4bd97803f44bb0474863b8008a69f3725956fd | ROOT-ADOPTED-WIRE-PINS.md | 103 | 5628 |
| a0a40804071a6dac83eaf6acf38073229a6d15c8866af32e283015d65c1c74e7 | ROOT-AUTHOR-INTERFACE.md | 110 | 6429 |
| 5629db5df0a37fdaecaa66f5ad0cde47006cb0c3047b37243b045daedef2ac29 | authority.py | 133 | 6496 |

Total 216102 bytes, 3473 lines. Read mode: parallel whole-file reads (one per file), then a second whole read of probe.py; no sections skipped.

Not read: any live peer output, the four scientific files other than authority.py, the old accepted dispatcher (f3e51286…) beyond its literal DISPATCH.diff, PINS.json, READ-SCOPE.md, ROOT card, git objects.

Writes: apply_patch only (four bounded patches to the report, one to this file plus one post-pin append). No Write/Edit/redirection, no input edit, no scientific subprocess.

## Post-read pins

All 13 inputs re-verified with `sha256sum -c` at 2026-09-11T03:57:57.871625579Z after every body read and after the A-C write: 13 OK, rc=0, identical to the pre-read table above. Every 64-hex token in both owned files was cross-checked against the live `sha256sum` output of the 13 inputs: 0 unmatched tokens. Correction note: the first post-pin append landed after the title because its anchor was a blank line; this patch moved the block here without changing its text. Final patch count: five to the report (skeleton, A-C, D-F/table/OPENS/collisions, one failed no-op attempt, attestation/marker) and three to this file (create, misplaced append, this move).
