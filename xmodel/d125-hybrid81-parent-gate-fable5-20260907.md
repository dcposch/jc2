# D125 hybrid81 parent-argv repair — independent delta gate (Fable5)

2026-09-07. Status: **UNSEALED — exact parent-argv delta CONFIRMED at mocked/static
scope; every actual-engine requirement remains GAP.** This review creates no
engineering GREEN, authority, deployment permission, production phase, solver
continuation, or mathematical exit-price claim. No engine was launched.

## 1. Scope and custody

I read all twelve frozen charged files in `/tmp/jc2-lane.Fwngeq/inputs` in full,
including both helpers (`engine.py` 86 lines, `original_engine.py` 73 lines),
`check.py`, the driver/checker/adapter modules, the registration, the patch,
`replay.json`, `custody.json`, both terminal reports, and the complete FALLACY-v2
text appended to the task. Every frozen file is byte-identical to its box or
`xmodel` original. I used no AWS, SSH, network, CAS, Singular, solver, authority,
production source, live report, or production host/path. Pre/post SHA-256 pins of
the frozen directory are identical, its listing is unchanged, and no bytecode
cache was created. The root-stated transaction, whole-proof, code, 24 pins and
94-case normal/-O checks are premises, not substitutes for this gate.

FALLACY-v2 applies no exit-price assertion here: this is a dispatch-predicate
review, so no `charge_basis` line is declared.

| Frozen input | Bytes | SHA-256 |
|---|---:|---|
| `engine.py` | 5,572 | `8d8da939caf88c75ae167fa6cf862011c76a593c105c88970efcd9baf16c7cdf` |
| `original_engine.py` | 4,850 | `a87debfce5ca01817c03c2b180fd514d8e45269b1173c6f4a562255883188ae5` |
| `driver.py` | 13,466 | `ce599a26a0ed051eddd71125f492bb0b19c4ef86cdf97a6bc887f5cf47cade5a` |
| `exact.py` | 11,088 | `7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9` |
| `hybrid.py` | 5,419 | `c9755a7172eaa7f1393860931d55c38a0b9d79b5b170eadbf14baff0203c35a3` |
| `REGISTRATION.md` | 4,680 | `364a5d8c57a967d6dc3467db13eb0b19ba6c7924a573dc5b3ea67da7eb6f1ee5` |
| `check.py` | 7,418 | `af50e7ff0ed1676a3f914bbdd46570444bc6109f5c9a39df31d5cf56eea1b76f` |
| `parent-argv.patch` | 1,910 | `9ecffb6966dd265ebca394763d4b886962f9f803a0aece70362077a02414c559` |
| `replay.json` | 1,288 | `e84d62d3c277913b2944d61604d9a3bbe6063cb802ce53ba0ff3164629b93ec9` |
| `custody.json` | 4,890 | `de220779c1768efb376b5c51bdb6caf6afd62a96cda3d0f7e2acd767a04078d3` |
| Sol56 v2 engine gate | 17,994 | `081d92293a62b0e5a9616e62b28d510468cfef4c6d6972d6926c66cca5c8e23d` |
| Astra parent repair | 6,014 | `94f71c4f20136cd585eee40b488797f7eee0a04a7337c6ab34e47c387a1153b2` |

## 2. Verdict per exact delta claim

| Claim | Verdict | Basis and boundary |
|---|---|---|
| The only production-code delta is the new pure `expected_parent_argv(operation)` plus one predicate replacement | **CONFIRMED** | `diff -u` shows exactly two hunks (`engine.py:43-54` inserted; `original_engine.py:52` replaced by `engine.py:65`); applying the charged patch to the frozen original reproduces `engine.py` byte-for-byte; D/E/H pins match `engine.py:11-13` |
| The expected vector is the registered 29-element parent command minus the outer `prlimit` exec prefix, for both literal operations | **CONFIRMED** | My own single-space split of `REGISTRATION.md:35`, a hand-written vector, and the helper function agree element-for-element for `hybrid` and `alarm` |
| All interpreter/flag/cap/cwd/output/child/authority slots, order, raw bytes, and exactly one final NUL are enforced | **CONFIRMED** at mocked scope | 94 charged cases plus 22 own cases; each rejection is attributed to the new predicate message with zero prior effects |
| Timer, limits, deadline, tiny parser/verifier, hashes, and exec are byte-for-byte unchanged | **CONFIRMED** | No other diff hunk; `driver.py`, `exact.py`, `hybrid.py` carry their original pins; the deadline sentinel receives the unchanged 7.0/1.0 (charged) and 3.5/1.0 (own) arguments |
| `check.py` is self-contained, passes normally and with `-O`, has zero Assert nodes, and includes an old-pass/new-fail caps/output countercontrol | **CONFIRMED** | Import closure is `check, engine, original_engine, driver, exact, hybrid` plus stdlib; stdout SHA-256 `9097ba47…5e92b470` in both modes, identical to the producer replay; Assert count 0 in all six files |
| Explicit tiny Singular syntax, seven I/T slots with `I_SIZE 4` and direct lift | **GAP** | No engine was run; nothing here bears on it |
| Inherited one-shot alarm, ready marker, and SIGALRM 14 termination | **GAP** | Mocked Python evidence cannot establish it |

## 3. The delta and the derived vector

The old predicate (`original_engine.py:52`) tested membership of the runner
pathname in the NUL-split parent command line, which the Sol56 v2 gate refuted
at its section 2. The new predicate (`engine.py:65`) requires
`read_bytes().split(b'\0')` to equal the 29 expected byte strings followed by one
empty string. Because a Linux command line is a sequence of NUL-terminated
elements, the only accepted byte string is the 29 elements joined and terminated
by exactly 29 NULs: 703 bytes for `hybrid`, 698 for `alarm`. A missing or extra
final NUL, an empty interior element, padding, case change, numeric respelling,
reordering, duplication, or a retained `prlimit` prefix all change the split and
reject.

Derived slots, index by index (the `alarm` vector differs only at 17, 19, 21, 27, 28):

- 0–3: `/usr/bin/python3`, `-I`, `-B`, `ROOT/run_capped.py`
- 4–13: `--wall-seconds 10`, `--cpu-seconds 10`, `--rss-bytes 536870912`,
  `--rss-sample-seconds 0.05`, `--term-grace-seconds 0.25`
- 14–15: `--cwd ROOT`
- 16–21: `--stdout-file ENG/OP.stdout`, `--stderr-file ENG/OP.stderr`,
  `--telemetry-file ENG/OP.telemetry.json`
- 22: `--`
- 23–28: `/usr/bin/python3`, `-I`, `-B`, `ROOT/engine.py`, `OP`, `ENG/OP.authority.json`

`ROOT` is `/home/ubuntu/d125-hybrid81-exact-solver-20260907` and `ENG` its
`engineering` child. The literal contains no quoting, so the charged `shlex`
derivation and my plain split agree. `OP` occurs in exactly five slots and not
inside `ROOT`, so the textual substitution is safe. The function re-checks the
operation literal, encodes ASCII only, and has no side effect.

## 4. Controls actually run

Each command used `timeout 30s`, `prlimit --cpu=25:25 --as=536870912:536870912
--fsize=67108864:67108864 --core=0:0`, and `/usr/bin/python3 -I -B`, with `-O`
added in optimized mode, invoked on the flat frozen directory without `cd`.
Python is 3.12.3. All four children returned 0 with empty stderr.

| Run | Wall | Peak RSS | stdout SHA-256 |
|---|---:|---:|---|
| charged `check.py` normal | 0.22 s | 26,696 KiB | `9097ba47ce0ac17eba9e4a5a318210df029238394791aba94389005b5e92b470` |
| charged `check.py` `-O` | 0.53 s | 29,976 KiB | same |
| own `fable_controls.py` normal | 0.16 s | 27,820 KiB | `2bda9bdd6c3ac8504ad0a6836057fd17bad635fa83b773b1784a4045d465a59a` |
| own `fable_controls.py` `-O` | 0.47 s | 30,612 KiB | `3ca24febc1abeaf926585e0cb89b86fee4e4b81d9a2cfc811a8b4a458978b543` |

The two own outputs differ only in the reported optimize flag. The charged run
reports 94 payload cases: two exact vectors reaching the deadline sentinel, 90
rejections at the new predicate, and two old-pass/new-fail caps/output objects.
Its attribution is strict: a rejection counts only when the message is exactly
`exact registered CAPRUN parent argv` and no effect was recorded, and the old
helper's probe would fail the run if the old predicate rejected. So the
countercontrol is non-vacuous, and `-O` cannot weaken it because no file contains
an `assert` or `__debug__`.

My own harness (`fable_controls.py`, SHA-256
`1c18e15daf1b94f66469b208614224844fbbbdf19572523378e406eb9b18b61c`) mocks the
same inputs independently, with different PIDs and a 3.5 s context duration, and
probes the real `payload` of both helpers. Per operation it runs eleven objects:

- `registered-exact`: accepted by both helpers, reaching the sentinel with the
  unchanged 3.5 (hybrid) or 1.0 (alarm) duration and no limit/write/exec effect.
- Old-pass/new-fail objects, all containing the runner pathname:
  `cross-operation-vector` (the other operation's full valid vector),
  `prlimit-prefix-retained`, `flag-case-changed` (`-i`), `padded-cap-value`
  (`10 `), `child-operation-swapped-only`, `child-interpreter-variant`
  (`python3.12`), `runner-token-alone`, `duplicated-vector`.
- Both-reject objects: `child-tail-alone`, `empty-cmdline`; the new helper still
  rejects at its own predicate.

These are mocked dispatch controls. They are not live CAPRUN or Singular
acceptance and prove nothing about same-UID adversarial isolation.

## 5. Observations outside the delta

- `driver.py:156-158` keeps the membership-style parent check for the generic
  driver payload. The engineering controls exec `engine.py`, not that path, and
  the Astra report says it is not newly authorized. This is unchanged scope, not
  a delta defect.
- The live predicate assumes the pinned runner keeps its exec-time argv area, as a
  Python process normally does. A rewrite, a reparented or zombie parent, or an
  empty command line all fail closed.
- The alarm parent vector keeps `--wall-seconds 10`; the one-second internal
  deadline is applied inside the payload via `min(duration,1.0)` as
  `REGISTRATION.md:26-31` prescribes.
- `ROOT` does not exist on this host; the mocks make path resolution non-strict
  and nothing was created there.

## 6. Unchanged live requirements

No root GREEN or production authority follows from this review. Root remains
responsible for retained-instance/EBS identity, fresh boot/process/resource and
output-absence custody, physical helper/D/E/H/fixture/CAPRUN/Singular/GREEN pins,
two distinct operation-bound authorities, generated-versus-live command comparison
captured promptly after spawn, exactly one `hybrid` then a conditional single
`alarm`, telemetry-first harvest with every byte retained, unchanged pre/post pins,
all-group terminal absence, and root STOP. No retries, cap enlargement, solver
phase, or production parsing follows. The typed GAPs in section 2 stay open until
those observations exist.

## 7. Owned artifacts

`box/d125-hybrid81-parent-gate-fable5-20260907/` holds `fable_controls.py`, the
four stdout/stderr/time captures, `PINS-pre.txt`/`PINS-post.txt` (identical),
the two identical input listings, `RUNS.json`, and `BOX-HASHES.txt`. No charged
byte was changed, no child process remains, and all writers are terminal.
**STOP/IDLE.**

<!-- BODY-END -->
