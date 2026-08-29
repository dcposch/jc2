# Hostile review: D43 exact sparse source rows v2

Date: 2026-08-28  
Reviewer: GPT-5.6, independent of the v2 producer  
Packet: `cases/d43_exact_sparse_rows_v2_20260828/`  
Review mode: bounded light local inspection/tests only; no D43 build, no local
CAS, no AWS, and no producer-packet mutation

## Verdict

**REPAIR — AWS launch is not authorized.**

The mathematical payload repairs are largely present and internally coherent:
the literal source-first a00pp collapse, EB refusal, canonical 432-coordinate
quotient-algebra output, exact B-block replacement, independent HW1/HW2/+42
controls, displayed E/E5/E6 bridge, and finite raw-J claim boundary all survive
this review.  The packet nevertheless fails its fail-closed operational
contract.  In particular, a bounded hostile fixture made finalization publish
a positive `VERDICT`, positive `FINAL_RECEIPT.json`, and `CURRENT_STAGE=COMPLETE`
before a later custody failure.  The shell then changes only `TERMINAL` to
`NO_VERDICT`, leaving contradictory positive authorities.  There is also no
exclusive one-run lock, no whole-job containment/orphan proof, no continuous
swap/resource monitor, and no immutable terminal archive.

No AWS action is authorized by this verdict.  Therefore there is no "first
authorized AWS action" for the present seal.

## Frozen inputs and seal replay

The supplied review identities were independently reproduced:

| Object | SHA-256 | Result |
|---|---|---|
| `SOURCE_V2.sha256` | `83635fe45e6f3a9e19d3c93ef963de769f2721653a7bb5333002dd100172fa73` | full 28-entry replay PASS |
| `PIPELINE_MANIFEST.json` | `6ae94434450d763c6ad89695f36f5eeccb394452805eff7a4aeeee6961705b43` | PASS |
| `OPERATIONAL_SOURCE.sha256` | `713555973c41d65d70d5dcbadfd5099255d5d8cd676324368cbc75981bdc4385` | full 14-entry replay PASS |
| `IMPLEMENTATION_REPORT_V2.md` | `05aa9a55ce85774ea91f4a1e414e5039b469a63241097168f3a93b8878f2d251` | PASS |
| `REVIEW_REQUEST_V2.md` | `b6edf9f30cc01980083df7b0a43aaf63d3c8f382adc2ddc7d9eb424284c76bf2` | PASS |
| prior hostile review | `283d47df4f55a0e83fbf1758cc8ac71fbe5ee8549dcdb1c3a6838c8ccc42b21e` | PASS |

The v1 packet remains present and its historical source-list digest
`9b851ede56986fe3154cf962f336fda6185fb7a4a00d07888c93e9b78a06848d`
replays.  Both the v2 preflight sidecar and the corrected historical v1
preflight sidecar replay.  I found no silent promotion of v1 evidence and did
not alter either packet.

## Bounded tests

The following were run without AWS or an external CAS:

* shell syntax check of `run_conditional_pipeline_aws_v2.sh`: PASS;
* byte compilation of the v2 producer, preflight, and tests to `/tmp`: PASS;
* `test_selected_rows_v2.py -v`: **13/13 PASS**, 7.55 s, about 111 MiB peak
  RSS;
* `test_d43_exact_sparse_source_preflight_v2.py -v`: **6/6 PASS**, 1.67 s,
  about 112 MiB peak RSS;
* hostile late-finalization fixture: reproduced contradictory terminal
  authorities;
* hostile optimized-Python fixture: a forged failing preflight receipt was
  accepted under `python3 -O` and rejected under ordinary Python.

No D43 side jet, D43 row, solver, or candidate was produced.

## Mathematical and semantic review

### 1. Literal source-first collapse and EB refusal: PASS

`convert_a_orbit` collapses each raw source coefficient before
`collapsed_gm_jet2` sees it (`selected_rows_v2.py:353-360`).  The adapter maps

```text
HW1^e1 HW2^e2 W1^a W2^b
  -> h^(e1+e2) W1^(a+e1) W2^(b+e2)
```

and returns only a `RadicalCoefficient` plus the two W exponents
(`d43_common_integral_emitter.py:234-274`).  A surviving EB exponent raises a
`ValueError` (`:249-255`).  The raw B/GB source census is checked before their
replacement (`selected_rows_v2.py:363-376`).  Thus the expensive A-side engine
does not retain independent HW generators, and EB cannot silently enter it.

### 2. Canonical K0 output and coefficient-ring wording: PASS, with one
required hardening item below

The normal form uses the monic triangular relations for zeta42, r3, A1, A2,
and h and the basis shape `12*2*3*3*2=432`
(`d43_common_integral_emitter.py:102-136`).  Because the five leading
monomials are in separate generator powers, reduction gives the claimed
canonical quotient-algebra coordinates.  The manifest correctly sets
`field_claim` to null, and the report calls K0 a quotient algebra rather than
asserting it is a field.  This packet does not need, and does not prove, that
the displayed 432-dimensional quotient is globally a field.

The bridge's claimed unit factor is legitimate even at the quotient-algebra
level: r3 has inverse `r3/3`, `r3+1` has inverse `(r3-1)/2`, and the remaining
factor C is a nonzero rational unit after `r3^2=3`.  Likewise A1, A2, and h are
units from their displayed relations.  Hence the bridge is not covertly
using the invalid implication "nonzero means unit" in a possibly non-field
algebra.

### 3. Exact B/GB collapse at D43: PASS

The literal B, GB42, and GB21 source series each contain only EB at source
level 12, with orbit sizes 42, 42, and 21.  Completing the seven phase factors
gives `(1+eta*t^20)^7-EB^7`; the frozen relation is `EB^7=3/2`.  The C7-block
multiplicities are 6 for a size-42 orbit and 3 for a size-21 orbit.  Therefore
the full blocks are exactly

```text
f: (((1+eta*t^20)^7 - 3/2)^6)
g: (((1+eta*t^20)^7 - 3/2)^(6+3))
```

at every truncation depth, not just at D21.  The implementation at
`selected_rows_v2.py:449-462` is consequently an exact source replacement.

### 4. Collapsed D21 equality and mutations: mathematical construction PASS;
literal gate needs REPAIR

The D21 payload is hash-checked before unpickling, filtered by literal source
names, remapped to the canonical registry, and passed through the same a00pp
adapter (`selected_rows_v2.py:837-862`).  HW1-only, HW2-only, and +42-omission
mutations are independently constructed (`:865-890`).  The three controls
have distinct canonical semantic digests in the light test, and the
inhomogeneous +42 appears exactly once in the real source-row formula
(`:495-515`).

However, the purported *exact equality* gate compares only SHA-256 digests at
`:867-884`; it never evaluates `rows == expected`.  A cryptographic digest is
excellent custody metadata but is not literal algebraic equality.  Before
launch, require direct structural equality of the canonical objects and
direct inequality for all three mutation objects, retaining the hashes only
as receipts.  Add negative tests that feed each independently mutated row set
through the actual gate and require refusal.

### 5. E plus unit and literal E5/E6 reconstruction: PASS in its stated scope

`template_bridge_spec` constructs

```text
E=(9+5*r3)A1 W1^4 + (9-5*r3)A2 W2^4,
W1 W2 uW12 - 1,
HM=-C a1^2 A1 W1^4/(4(a1-4)),
s1F=(2^8/7^16)HM.
```

It then checks as canonical quotient-algebra identities that E5_1 is zero,
E5_2 is `C*r3*(r3+1)*E`, and the displayed E6 cube row is zero
(`selected_rows_v2.py:894-943`).  The product-unit row makes both W1 and W2
units; the formulas above make HM and s1F units.  Both banked primes replay E,
the product-unit equation, literal E5/E6, and HM/s1F nonvanishing
(`:967-1043`).

This is elimination-equivalent to the **displayed** E5/E6 existential
subsystem after localizing at W1W2; it is not evidence for omitted
residue-A/template equations.  The report and manifest maintain that boundary
and correctly say the row emitter itself does not impose E or the unit row.

### 6. Side independence and one-process conditional emission: semantic code
PASS, run custody REPAIR

The two side payloads carry manifest, preflight, operational-root, registry,
support, coefficient-algebra, semantic, PID, host, and interval metadata
(`selected_rows_v2.py:642-693`).  Pair assembly requires different PIDs on the
same registered hostname and overlapping closed time intervals (`:735-800`).
`conditional_emit_all` loads that pair once, performs the band-20 gate, and
only then creates all 19 disjoint shards and the 184-row merge in the same
Python invocation (`:1104-1211`).  This is the intended mathematical control
flow.

It is not yet an immutable *run* because duplicate wrappers can race and
overwrite the same fixed f/g/pair/output paths.  In that race the final pair
can combine receipts produced by different wrapper invocations while still
satisfying distinct-PID and overlapping-time checks.  The semantic design
passes; operational exclusivity must be repaired.

### 7. The 155/29 forecast: acceptable only as a preregistered future gate

The packet contains no v2 D43 rows and does not claim otherwise.  The light
test for 155/29 constructs a synthetic inventory; it is an interface test, not
evidence for the forecast.  On a real run, `validate_exact_inventory`
requires literal empty canonical row dictionaries for exactly 155 targets,
29 live rows confined to bands 20/30/40 with distribution 10/9/10, and degree
at most two (`selected_rows_v2.py:1046-1063`).  Thus a passing real gate would
establish the finite inventory rather than infer it merely from two modular
specializations.

The report's wording "the real run must prove" is acceptable.  Future reports
must continue to label 155/29 as a forecast until such a sealed D43 run exists.
The gate is deliberately hypothesis-selective: if exact output differs, the
result is `NO_VERDICT` for this preregistered branch, not a proof that the exact
emitter is mathematically wrong.

### 8. Solver and claim scope: PASS

The manifest authorizes side construction and conditional row emission but
sets `solve=false`; no solver is present or invoked.  A successful emission
would certify only a finite, support-specialized, pure-y, alpha=beta=0 set of
184 raw-J rows over the stated quotient algebra.  It would not certify a
raw-J point, the E/unit extension, full residue-A/template membership, the
banked NF presentation, all-depth compatibility, a Keller map, or a JC2
counterexample.  The report's claim tiers preserve these distinctions.

## Launch-blocking operational defects

### A. Duplicate wrappers can pass preflight and corrupt same-run custody

`aws_preflight_v2.py:82-109` ignores ancestors and flags another same-UID
process only when its RSS is at least 1 GiB or its command contains one of six
tokens.  Neither `run_conditional_pipeline_aws_v2.sh` nor
`aws_preflight_v2.py` is a token, and there is no exclusive lock.  Two wrappers
started together can therefore both pass while both are still low-RSS
preflight processes, then race on identical paths.  The test at
`test_selected_rows_v2.py:175-179` only proves removal of the old textual
same-directory exemption; it does not test this race.

Required repair: acquire a one-shot kernel-backed exclusive lease before any
preflight or output mutation (for example `flock -n` on a host/job-specific
sealed lock, plus an atomic fresh-run marker).  Refuse any run directory that
already has stage, output, or terminal artifacts.  Add the wrapper/preflight
tokens to the census as defense in depth, but do not treat a process-name scan
as the primary lock.  Bind the lease/run nonce into every receipt.

### B. There is no whole-job containment or orphan proof

The wrapper backgrounds shell functions at
`run_conditional_pipeline_aws_v2.sh:68-80`, has no trap, process-group/cgroup
creation, cleanup, or terminal no-orphan census, and uses
`timeout --foreground` (`:42`, `:106`).  Killing the supervisor can leave
workers alive; failure of one side waits for the other instead of cancelling
the entire job.  Per-process `prlimit` is not a whole-job boundary.

Required repair: run the complete route in a uniquely identified cgroup v2 or
equivalent whole-job scope with kill-on-supervisor-exit semantics.  Install
TERM/INT/HUP/EXIT traps that kill and reap the complete job tree; on either
side's failure, cancel and reap its peer.  Record the cgroup identity and
events, and require `populated=0`/no matching job processes before any
terminal receipt.  Add hostile supervisor-kill, timeout, worker-failure, and
orphan tests.

### C. Swap and resource enforcement is only point-in-time/per-process

`zero_swap` runs only before and after long stages (`run_conditional...:24-29,
39-50,84,103,117`).  A swap violation during a 24-hour stage can disappear
before the next observation.  There is no sticky monitor.  Address-space and
file limits are per process, not aggregate; there is no cgroup memory/pids
limit, OOM-event receipt, or continuous RSS/swap telemetry.

Required repair: enforce `memory.swap.max=0` for the job cgroup and run a
sticky monitor for host swap configuration/use and aggregate cgroup memory.
Any monitor death or observed drift must atomically latch `NO_VERDICT`.  Bind
the configured limits, `memory.events`, peak usage, monitor receipt, timeout
status, and final empty-cgroup census into terminal custody.  Exercise
timeout, OOM/resource, monitor-death, and transient-swap hostile fixtures.

### D. Positive terminal authority is published before custody completes

`finalize_run` writes positive `VERDICT`, positive `TERMINAL`,
`CURRENT_STAGE=COMPLETE`, and positive `FINAL_RECEIPT.json` at
`selected_rows_v2.py:1228-1244`.  Only afterward does it enumerate/hash
artifacts and write `ARTIFACTS.json` (`:1245-1257`).  If that later work fails,
the wrapper's `fail_terminal` changes only `TERMINAL`
(`run_conditional...:31-34,116`), leaving the other positive files intact.

A bounded fixture forced `sha256_path` to fail on the first inventory hash.
The observed state immediately after the exception was:

```text
VERDICT = EXACT_A00PP_184_RAW_J_ROWS_EMITTED_NO_SOLVE
TERMINAL = D43_A00PP_EXACT_ROW_PIPELINE_COMPLETE
CURRENT_STAGE = COMPLETE
FINAL_RECEIPT.json = present and positive
ARTIFACTS.json = absent
```

After modeling `fail_terminal`, only `TERMINAL` changed to
`NO_VERDICT_FINAL_CUSTODY`; the positive verdict, positive final receipt, and
COMPLETE stage remained.  This is a demonstrated fail-open terminal split,
not a stylistic concern.

Required repair: use one authoritative terminal object.  Prepare and verify
all payloads, source/registration/preflight receipts, final inventory, and
archive before publishing it.  Publish a positive authority exactly once and
last by atomic rename.  On any earlier or late failure, publish only an
authoritative `NO_VERDICT` object and ensure no positive authority exists.
Add a hostile failure injection at every finalization boundary and after every
write/rename.

### E. There is no immutable archive or replayed archive custody

The wrapper never creates an archive.  `ARTIFACTS.json` inventories a mutable
live directory and is itself written after positive terminal markers.  There
is no deterministic source/run archive, archive SHA sidecar, reopen/replay
test, or binding of a terminal authority to an archived byte sequence.

Required repair: create a deterministic immutable run archive containing the
registered operational source packet, registration/preflight records,
resource/process receipts, mathematical payloads, and provisional inventory;
write a SHA-256 sidecar, reopen it, validate its exact member set and hashes,
and bind its digest into the single terminal object.  Archive failure is
`NO_VERDICT`.  Keep the v1 packet and sidecars unchanged.

### F. Fail-closed validation disappears under optimized Python

Manifest, receipt, pair, shard, inventory, and algebra validation use many
Python `assert` statements.  The wrapper happens to invoke `python3 -B`, but
the entry points themselves are not fail-closed under `python -O`.  A bounded
fixture supplied a receipt with schema `FORGED`, `pass=false`, wrong manifest
hash, wrong source-list hash, and empty live identity/tag.  The result was:

```text
python3 -O: OPTIMIZED_ACCEPTED FORGED False WRONG <receipt-sha256>
python3:    NORMAL_REJECTED AssertionError
```

Required repair: replace all authorization, custody, semantic, and algebraic
`assert` uses on production paths with explicit exceptions.  Add a hostile
`python3 -O` suite proving identical refusal behavior.  Unit-test assertions
may remain assertions in the test framework.

## Required repair set for rereview

1. Add literal object equality to the D21 gate and direct rejection tests for
   the three independent mutations.
2. Replace production-path authorization/custody/semantic asserts with
   explicit fail-closed checks, including optimized-Python tests.
3. Enforce a fresh, exclusive, one-shot run lease before preflight and bind a
   run nonce/lease identity into all receipts.
4. Put the complete wrapper and descendants in a job-wide containment scope;
   cancel/reap peers and prove no orphans on every terminal path.
5. Enforce aggregate memory/pids/swap limits and sticky continuous monitoring;
   bind timeout/OOM/swap/monitor facts into custody.
6. Stage all final custody before a single positive terminal publication.
   Every failure path must leave only one unambiguous `NO_VERDICT` authority.
7. Create, hash, reopen, and fully replay a deterministic immutable run
   archive before terminal publication.
8. Add bounded hostile tests for duplicate launches, stale-directory reuse,
   supervisor death, orphan survival, peer failure, timeout, OOM, transient
   swap, monitor death, late finalization failure, archive corruption, and
   optimized Python.
9. Preserve the existing v1 packet and sidecars.  Seal the repaired sources,
   tests, preregistration, review request, and operational route under new
   versioned hashes; do not mutate this reviewed v2 seal in place.

## Conditional first AWS action after a future PASS

For avoidance of ambiguity: **none is authorized now**.  If a new sealed
revision receives an independent hostile PASS, its first AWS action should be
only to stage that exact sealed revision into a fresh, unique, empty job
namespace on an otherwise idle registered high-memory EC2 host and create the
host-specific immutable manifest/registration/one-shot lease inputs.  The
heavy wrapper must not start until those staged bytes, the live IMDSv2
identity/tag, the exclusive lease, the zero-swap cgroup, and the operational
source list all replay exactly.
