# d125 hybrid81 caller repair — independent hostile DELTA gate (Sol56)

Status: **SEALED — POSTHASH-RECEIPT CONFIRMED; DEADLINE-HANDOFF
CONFIRMED for the generic Linux/Python path; pinned-Singular startup/alarm behavior
remains GAP.** No solver or deployment authority is created.

## 1. Bounded scope and custody

I read all ten charged files in `/tmp/jc2-lane.q9z0fq/inputs` in full and read
the complete FALLACY-v2 text appended to the task charge. I used no live peer,
ledger, protected tree, network, AWS, SSH, CAS, solver, production source,
authority file, or actual engine. No frozen byte was edited. No mathematical
exit-price assertion is made.

The charged root facts — author IDLE, transaction
`27e1636db0a6918aec6c3d137be122cee9a576f8941118147e0571e7ae69a720`,
root test receipt
`a596d11102f2b00e57cb0946d3447476ac1e4efe3011672170b4216146d030e2`,
12 unchanged owned pins, and 31 methods per normal/optimized mode in 12.547
seconds — remain custody premises, not proof authority. The supplied caller
report independently hashes to its charged
`feb918be39485ad3bd2377397122787ea149c402333d9f477367e577bfeff256`.

All frozen sizes and full SHA-256 values are recorded in `PINS.json`, SHA-256
`a0f457d3569d16393e2a410083f368901f67b9ea181654b8834bf997aae2067b`.
Key independently checked pins are repaired `driver.py`
`ce599a26a0ed051eddd71125f492bb0b19c4ef86cdf97a6bc887f5cf47cade5a`,
`exact.py` `7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9`,
`hybrid.py` `c9755a7172eaa7f1393860931d55c38a0b9d79b5b170eadbf14baff0203c35a3`,
and the tiny JSONL
`d00df83bafddcd3436dad44034bdb1680d306f6d67f8bfa83d4b32de19961bbf`.

## 2. Exact delta confinement

**CONFIRMED.** I reversed only the five mechanical manifestations of the two
named repairs in the frozen new source: the signal import, `arm_deadline`
definition, immediate payload call, two receipt predicates, and movement of the
post-hash check before publication. The resulting in-memory old byte object
hashes to the charged old SHA-256
`faf7a1e08fa7fafac09160b57587eb325ef4542da30a7defbf5165bc329569d9`.
Reapplying the supplied changed-line payload produces the exact new bytes and
SHA above. Thus there is no additional code delta between those anchored
objects.

There is one non-code patch-format note. Frozen `driver-two-bugs.patch`, SHA-256
`5daab0735fd9fceb83acf6886a4364c3f533c7fb67dc88baea7885526a7ce2df`,
ends after `return result.returncode`; its final hunk header counts two following
blank context lines which are not physically present at patch EOF. Its added and
deleted lines match the complete object diff exactly, and GNU `patch --dry-run
--reverse --force` accepted the frozen new target with exit 0. This elision is
not an extra source change and does not alter either repair verdict.

The delta does not change the exact-certificate format, full-source coverage,
footer, `limits`, adapter, source cap, phase cap values, CAPRUN command, or
accepted runner hash constant. The underlying CAPRUN bytes were unavailable and
were neither read nor run; their accepted status is a scoped dependency.

## 3. POSTHASH-RECEIPT path

**CONFIRMED.** In the repaired object, non-control launch computes the actual
post-run source hash, requires the exact object
`{'jsonl': H.CONSTRUCTION_SHA}`, and only then exclusively creates
`<phase>.result.json` (`driver.py:224-229`). Verify requires both
`receipt.phase == 'decision'` and that exact one-key post-source-pin object
(`driver.py:171-174`). Missing or extra keys do not compare equal.

Actual tiny filesystem controls used the exact reconstructed old and frozen new
driver objects. With mocked child return 0 and a real mismatching source file,
the old object created `decision.result.json` and then rejected; the repaired
object rejected with no result receipt. With the exact tiny source, the repaired
object returned 0 and published the exact decision phase/post-pin object.

Actual verification paths then used hashed identity, telemetry, stdout, stderr,
result files, and a mathematically valid tiny exact-Q cofactor stream. The old
object accepted each of seven bad receipts: control, verify, or missing phase,
and wrong, empty, extra-key, or missing post-pin objects. The repaired object
rejected all seven at `decision custody/return/source status`; the exact
decision/one-key object still reached
`EXACT_Q_UNIT_COFACTOR_CERTIFICATE`. This confirms the named ordering and
readback contract, not atomic filesystem immutability or broader controller
policy.

## 4. DEADLINE-HANDOFF path

**CONFIRMED for the generic Linux repair.** `payload` calls `arm_deadline`
immediately after `context` and before process checks, limit setup, identity
serialization, source read, parsing, certificate arithmetic, or exec
(`driver.py:152-166`). The arm path installs `SIG_DFL`, unblocks `SIGALRM`,
freshly computes `min(duration, end-time.time())`, rejects a nonpositive value
instead of passing the zero/disarm value, and makes the source's only
`setitimer(ITIMER_REAL, ...)` call (`driver.py:142-149`). There is no reset.

Normal and optimized real subprocess controls began with SIGALRM ignored and
blocked and inserted a 0.20-second context delay into a 0.75-second absolute
deadline. On the delayed-parse path, the old object had no timer, printed
`PARSE_DONE`, and returned 1.181216/1.243035 seconds after deadline. The repaired
object showed 0.546022/0.546153 seconds remaining on entry and died by signal 14
before `PARSE_DONE`; parent-observed return lag was 1.626/2.038 ms.

On the actual same-PID Python `execve` path, the old object retained the
ignored/blocked state, had no timer, and survived 0.381303/0.444444 seconds past
deadline. The repaired executable observed default/unblocked SIGALRM and a live
decreasing timer of 0.423023/0.360751 seconds, then died by signal 14 without a
`SURVIVED` marker; return lag was 0.677/1.121 ms. All children were reaped.

These observations establish the Linux/Python exec path, not a hard real-time
scheduling guarantee. The claim is limited to payload deadline arithmetic and
the unchanged relative phase wall/CPU/group-RSS caps. Parent-side terminal
post-hash and receipt harvesting are outside that arithmetic. No claim is made
about arbitrary administrator clock jumps after conversion to a relative timer.

## 5. Focused controls and immutable surfaces

`gate_checks.py`, SHA-256
`6006db6bea500abc12182b33db07dd9e1ba6767f4f0bb6a8645ddb9c8799c816`,
ran 33 named outcomes in each mode with `-B` before imports and no AST `Assert`
in the gate or implementation modules. Each batch was externally bounded by 30
wall seconds, 25 CPU seconds, and 512 MiB address space:

| Mode | Result | Wall | Self + child CPU | Peak self/child RSS |
|---|---:|---:|---:|---:|
| normal | 33/33 PASS | 5.019234 s | 0.466093 s | 29,412/29,412 KiB |
| `-O` | 33/33 PASS | 6.481587 s | 1.990016 s | 31,972/31,972 KiB |

The tests independently rehashed all ten frozen files before and after. Exact
commands, outcomes, metrics, and probe observations are in `RUNS.json`, SHA-256
`0a42d8b7a459cdcd78b744fc9708b1fa5b32ab6d0e62d26201fc90bcbeebfc`.
The unavailable old upstream test paths were not accessed; these are own focused
path adaptations. No enforcement depends on removable language assertions.

The unchanged footer and limits follow from the exact confined object diff;
the unchanged adapter and exact checker follow from their frozen byte pins.
Accordingly, this gate does not silently re-harden or reopen accepted certificate
criteria, full-source transport, unchanged resource limits, or the 2 MiB input
cap.

## 6. Fixture boundary and residual GAPs

The supplied 1,698-byte tiny JSONL is reusable. I parsed it and derived the
unchanged `footer(..., control=True)` input in memory only: 1,072 bytes, SHA-256
`59295067207d4f17eb2acdbd4eac9d4755d16c94bfc36884e2f14d2731b9ad11`,
four variables and seven rows. It contains no `slimgb(I)`, substitutes exactly
one `ideal G=ideal(1)`, and uses exactly one direct
`lift(I,ideal(1))`. **ENGINE NOT RUN.**

The prior report says its saved 1,073-byte `.sing` uses the production
`slimgb(I)` footer and has SHA-256 `d1c334443efb9d31eedc6a821970ce990f9ba9a551b6c8c94fa4411ab4904b2e`.
That saved file was not supplied here, was not independently hashed, and was not
executed. It must not be reused as the later engineering control.

Exact residual verdicts:

| Boundary | Verdict | Meaning |
|---|---|---|
| New driver contains only the two named repairs | **CONFIRMED** | Old/new byte hashes and complete changed-line payload agree. |
| Source post-hash before exclusive receipt publication | **CONFIRMED** | Mismatch leaves no result; match publishes the exact pin. |
| Exact decision phase and post-pin readback | **CONFIRMED** | Seven malformed variants reject; exact object passes. |
| Fresh one-shot timer through same-PID Python exec | **CONFIRMED** | Normal and optimized real-kernel paths die by SIGALRM. |
| Actual pinned Singular startup/alarm interaction | **GAP** | Generic Python exec supplies no engine guarantee. |
| Actual Singular syntax/index/direct-lift control | **GAP** | No engine was run under this gate. |
| Actual 81-variable generated size | **GAP** | Full source was unavailable and not read. |

No requested delta path is REFUTED. The remaining engine gap does not refute the
generic Linux fix; it limits its promotion scope.

## 7. Gate disposition

The two named caller repairs are independently **CONFIRMED** at their stated
scope. Root must separately authorize pinned-engine index/alarm testing. Any
later tiny engineering control must be freshly derived with `control=True` and
direct lift-to-one only. Only after that separate gate may root consider one
300-second full decision, optional 120-second verify, 450-second aggregate,
16 GiB AS/RSS, 64 MiB streams, and 2 MiB generated-input workflow. This report
authorizes none of those engine, solver, worker, deployment, or source actions.

All owned writers and timed children are terminal. **STOP/IDLE.**

<!-- BODY-END -->
