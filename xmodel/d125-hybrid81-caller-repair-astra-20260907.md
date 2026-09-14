# Hybrid81 caller: two versioned lifecycle repairs

2026-09-07. Author `/root/model_productivity`. **LOCAL PREP ONLY / PENDING
SCOPED INDEPENDENT DELTA GATE.** Sol's terminal report
`xmodel/d125-hybrid81-solver-gate-sol56-20260907.md`, SHA
`b4198c3689e0d713eca6a1a7dfe95854f88bb48f45217b737adb29e03c4fcc46`,
was read whole. Its two named caller defects are corrected in new
`box/d125-hybrid81-caller-repair-20260907/` (below, B). No frozen file changed.
No CAS, AWS/SSH, worker, production stream, deployment or authority was used.

## Exact narrow delta

Old driver SHA remains
`faf7a1e08fa7fafac09160b57587eb325ef4542da30a7defbf5165bc329569d9`.
New driver SHA:
`ce599a26a0ed051eddd71125f492bb0b19c4ef86cdf97a6bc887f5cf47cade5a`.
The complete diff is B/driver-two-bugs.patch, SHA
`5daab0735fd9fceb83acf6886a4364c3f533c7fb67dc88baea7885526a7ce2df`.

**POSTHASH-RECEIPT.** The post-source hash is now validated before the exclusive
result publication. A mismatch leaves no result receipt. Verification additionally
requires `receipt.phase == 'decision'` and the exact object
`receipt.source_pins_after == {'jsonl': H.CONSTRUCTION_SHA}`. Missing, incorrect
or extra post-pin keys fail. A later restored current source does not excuse a
bad decision receipt. Raw partial outputs remain available for custody; no old
result is overwritten/deleted or promoted.

**DEADLINE-HANDOFF.** The payload calls new arm_deadline immediately after context,
before source reads, identity serialization or arithmetic. It installs default
SIGALRM disposition, unblocks SIGALRM, then computes
`min(duration, deadline_timestamp - time.time())` freshly at arming time. Thus
context/host/binary-hash delay cannot preserve an earlier longer allowance.
Nonpositive remaining time is rejected, not passed as a zero/disarming timer.
A single ITIMER_REAL wall timer covers parsing, serialization, verification and
the exec-in-place engine handoff. There is no later reset or refresh.

The reviewed exact.py (`7ca2b24e…`), hybrid.py (`c9755a71…`), old footer,
limits function, registry, every source row, Q/dp order and certificate criteria
are unchanged. Tests verify exact/adapter byte pins and footer/limits source
equality. Accepted CAPRUN `4435279d…` was neither copied anew nor edited/run.
All phase/aggregate/resource/exclusive-output limits remain unchanged.

## Timer semantics and boundary

Linux [setitimer(2)](https://man7.org/linux/man-pages/man2/setitimer.2.html)
documents wall-clock SIGALRM and explicitly preserves interval timers across
execve. The default action is termination, per
[signal(7)](https://man7.org/linux/man-pages/man7/signal.7.html).
[Python's signal API](https://docs.python.org/3/library/signal.html#signal.setitimer)
supports fractional seconds and a one-shot timer; zero would disable it.
B/alarm-semantics.md records the narrow documentation/source perimeter.

This is Linux timer enforcement, not a hard real-time scheduling theorem:
kernel delivery/wait can lag the deadline slightly. The450-second budget is
for payload arithmetic and phase caps; parent terminal post-hash/receipt harvest
can finish afterward. CAPRUN independently retains wall/CPU/sampled-group-RSS
and cleanup enforcement. The clock-to-relative-timer conversion is made at arming;
no claim about arbitrary subsequent administrator clock jumps is made.

The real exec test here runs Python, not Singular. It proves preservation and
deadline action through the actual kernel exec path. A pinned-Singular startup/
alarm interaction is still a specifically named later engineering check, not
pretended completed. Limited upstream searches in ipshell.cc/fevoices.cc were
not treated as a whole-program or pinned-binary guarantee.

## Actual old-versus-new controls

All25 unchanged existing methods and six new caller methods passed in normal
and optimized Python. The new methods execute actual file receipt paths with
tiny mocked host/context/child completion, plus real Linux timed subprocesses:

- With child return0 and an actual mismatching tiny source file, the old launch
  publishes a receipt and then rejects; the new launch rejects with no result.
  Matching tiny source still publishes the exact phase/post-pin object.
- Old verification accepts synthetic, mathematically valid toy certificates
  with phase control/verify, wrong/empty/extra post-source objects. New verification
  rejects each at the custody check; the correct decision receipt still passes.
- A declared0.75-second absolute deadline includes a0.20-second context delay.
  In delayed parsing, the old process completes parsing after expiry and survives;
  the new process receives SIGALRM before PARSE_DONE.
- In the real exec variant, the old program survives beyond expiry. The repaired
  same-PID executable reports an active decreasing timer and default SIGALRM,
  then receives signal14 before its SURVIVED marker. Tests start SIGALRM both
  ignored and blocked to exercise the repaired disposition/mask setup.

Final repaired deadline delivery/wait lags were1.441/1.763ms in parse controls
and0.768/0.678ms after exec (normal/optimized). Old return times were about1.381s
and0.581s beyond the respective deadlines. All timed children were reaped and
their exact PIDs absent. These are declared tiny no-CAS integration probes, not
mocked timer signals or actual worker/engine evidence.

Two bounded batches were retained: the first passed, then the test log/check was
extended to record and bound actual return lag. Final31-method batches passed
in both modes in12.521157s,2.645340 child CPU seconds,29868KiB peak child RSS.
Both batches together used25.050054s wall and5.294507 child CPU, max29872KiB,
within30wall/25CPU/512MiB. No enforcement uses removable language assertions.
Final evidence B/test-results.json SHA
`c9bee29178d6d0d9273b1fb47a6e369a2270adcafe2ff7825cd5a19d18d38bd5`.
Replay command is `python3 -B B/run_tests.py`; it creates only declared temporary
toy test files and children, not authority or production output.

## Existing Sol fixture and next boundary

The existing Sol tiny JSONL was reused in place, SHA
`d00df83bafddcd3436dad44034bdb1680d306f6d67f8bfa83d4b32de19961bbf`.
Its1698 bytes describe the rational four-variable/seven-slot zero/duplicate/
inverse-guard fixture. No duplicate fixture was invented.

Important mismatch: Sol's1073-byte `.sing`, SHA
`d1c334443efb9d31eedc6a821970ce990f9ba9a551b6c8c94fa4411ab4904b2e`,
contains the **production footer with slimgb(I)**. It was only hash-checked and
byte-compared against the unchanged serializer, never executed. Later
engineering must derive `control=True` footer from the pinned JSONL and must
not execute that saved production-footer file as an engineering input.

Independent Sol delta review of these two caller changes remains required.
Actual tiny Singular syntax/index/alarm behavior and actual production generated
size under the unchanged2MiB cap remain pending separate root authority. There
is no new full algebraic source-replay gate, solver result or JC2 claim.

All12 local artifact pins, old/new/source fixture dependencies and measured tests
are in B/custody.json, SHA
`386ea7a8250f0b08c661d1066729ef3b5a968dd1783d4813bb13c79e2c0f00e9`.
All original code and Sol fixture hashes were rechecked unchanged after tests.
Every owned child/writer is terminal. **SEALED / STOP / IDLE.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7367`.
- Body SHA-256:
  `21ea23bd5272f5bb5c03118c595f43451f79dcf730ff375f3146e20ba7c30e4f`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
